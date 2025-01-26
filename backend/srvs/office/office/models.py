import re
from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
from django.core.cache import cache
from pormalizer import Pormalizer
from shapely.geometry import Point, Polygon
from backend.srvs.office.office._settings import (
    PRICE_MIN,
    PRICE_MAX,
    RENT_MIN,
    RENT_MAX,
    BUILT_YEAR_MIN,
    BUILT_YEAR_MAX,
    KILOMETER_MIN,
    KILOMETER_MAX,
)
from backend.libs.log import log
from backend.srvs.office.gate.models import User

pormalizer = Pormalizer()

def normalize(addr: str):
    normalized_addr = pormalizer.normalize(addr)
    return (normalized_addr.replace(" ", "").replace("-", "")
            .replace(",", "").replace("،", "").replace("(", "")
            .replace(")", "").replace("‌", ""))


class City(models.Model):
    name = models.CharField(
        max_length=100
    )
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


def change_polygon(old_polygon: str) -> str:
    pattern = r'\((\d+\.?\d*),(\d+\.?\d*)\)'
    polygon_list = re.findall(pattern, old_polygon)
    new_poly = []
    for point in polygon_list:
        x = float(point[1])
        y = float(point[0])
        new_poly.append((x, y))
    new_poly.append(new_poly[0])
    new_polygon = "(" + str(new_poly)[1:-1].replace(" ", "") + ")"
    return new_polygon


class District(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    city = models.ForeignKey(
        City,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    polygon = models.TextField(
        null=True,
        blank=True,
    )

    def fix_polygon(self):
        self.polygon = change_polygon(self.polygon)
        self.save()

    def __str__(self):
        return self.name


class Neighborhood(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='neighborhoods',
    )
    polygon = models.TextField(
        null=True,
        blank=True,
    )

    def fix_polygon(self):
        self.polygon = change_polygon(self.polygon)
        self.save()

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.TextField()
    latitude = models.FloatField(
        null=True,
        blank=True,
    )
    longitude = models.FloatField(
        null=True,
        blank=True,
    )
    priority = models.IntegerField(null=False)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=100,
    )

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=100,
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="car_models"
    )

    def __str__(self):
        return self.name


class Post(models.Model):
    class Color(models.IntegerChoices):
        WHITE = 1
        BLACK = 2
        GRAY = 3
        SILVER = 4
        PENCIL_TIP = 5
        BLUE = 6
    class Gearbox(models.IntegerChoices):
        AUTOMATIC = 1
        RIBBED = 2
    class RentType(models.IntegerChoices):
        HOURLY = 1
        DAILY = 2
        WEEKLY = 3
        MONTHLY = 4

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    color_id = models.IntegerField(
        null=True,
        choices=Color.choices,
    )
    gearbox_id = models.IntegerField(
        null=True,
        choices=Gearbox.choices,
    )
    is_offroad = models.BooleanField(
        null=True,
        blank=True,
    )
    price = models.BigIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(PRICE_MIN),
            MaxValueValidator(PRICE_MAX),
        ],
    )
    rent_type_id = models.IntegerField(
        null=True,
        choices=RentType.choices,
    )
    rent = models.BigIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(RENT_MIN),
            MaxValueValidator(RENT_MAX),
        ],
    )
    built_year = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(BUILT_YEAR_MIN),
            MaxValueValidator(BUILT_YEAR_MAX),
        ],
    )
    kilometer = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(KILOMETER_MIN),
            MaxValueValidator(KILOMETER_MAX),
        ],
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    car_model = models.ForeignKey(
        CarModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="posts",
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="posts",
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    neighborhood = models.ForeignKey(
        Neighborhood,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    public_address = models.CharField(
        null=True,
        blank=True,
        max_length=100,
    )
    private_address = models.CharField(
        null=True,
        blank=True,
        max_length=100,
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )
    latitude = models.FloatField(
        null=True,
        blank=True,
    )
    longitude = models.FloatField(
        null=True,
        blank=True,
    )

    def find_neighborhood_district(self):
        if not self.latitude or not self.longitude:
            return
        else:
            point = Point(self.latitude, self.longitude)
        neighborhoods = cache.get("neighborhoods")
        sw = True
        if not neighborhoods:
            neighborhoods = Neighborhood.objects.all()
            cache.set('neighborhoods', neighborhoods)
        for neighborhood in neighborhoods:
            polygon_str = neighborhood.polygon
            pattern = r'\((\d+\.?\d*),(\d+\.?\d*)\)'
            polygon_list = re.findall(pattern, polygon_str)
            poly = []
            for point_ in polygon_list:
                x = float(point_[0])
                y = float(point_[1])
                poly.append((x, y))
            if len(poly) < 4:
                pass
            else:
                polygon = Polygon(poly)
                if point.within(polygon):
                    self.neighborhood = neighborhood
                    self.district = neighborhood.district
                    self.city = neighborhood.district.city
                    if self.city != neighborhood.district.city:
                        log.error(f"old city {self.city} with new city {neighborhood.district.city}"
                                  f"does not match")
                    sw = False
                    break
        if sw:
            districts = cache.get("districts")
            if not districts:
                districts = District.objects.all()
                cache.set("districts", districts)
            for district in districts:
                polygon_str = district.polygon
                pattern = r'\((\d+\.?\d*),(\d+\.?\d*)\)'
                polygon_list = re.findall(pattern, polygon_str)
                poly = []
                for point_ in polygon_list:
                    x = float(point_[0])
                    y = float(point_[1])
                    poly.append((x, y))
                if len(poly) < 4:
                    pass
                else:
                    polygon = Polygon(poly)
                    if point.within(polygon):
                        self.district = district
                        self.city = district.city
                        if self.city != district.city and self.city:
                            log.error(f"old city {self.city} with new city {district.city}"
                                      f"does not match")
                        break

    def find_place(self):
        pub_address = self.public_address
        place = None
        normalized_title = normalize(self.title)
        normalized_description = normalize(self.description)
        if pub_address:
            places = cache.get('places')
            if not places:
                places = Place.objects.all().order_by('priority')
                cache.set('places', places)
            normalized_addr = normalize(str(pub_address))
            selected_place = None
            selected_place_title = None
            selected_place_description = None
            for place_ in places:
                normalized_place_name = normalize(place_.name)
                if normalized_place_name in normalized_addr:
                    selected_place = place_
                    break
                elif normalized_place_name in normalized_title:
                    if selected_place_title:
                        if selected_place_title.priority > place_.priority:
                            selected_place_title = place_
                    else:
                        selected_place_title = place_
                elif normalized_place_name in normalized_description:
                    if selected_place_description:
                        if selected_place_description.priority > place_.priority:
                            selected_place_description = place_
                    else:
                        selected_place_description = place_
            if selected_place:
                place = selected_place
            elif selected_place_title:
                place = selected_place_title
            elif selected_place_description:
                place = selected_place_description
        self.place = place
        if place:
            self.latitude = place.latitude
            self.longitude = place.longitude

    def save(self, *args, **kwargs):
        if not self.place and (not self.latitude or not self.latitude):
            self.find_place()
            self.find_neighborhood_district()
        elif self.place and (not self.latitude or not self.latitude):
            self.latitude = Place.objects.get(id=self.place.id).latitude
            self.longitude = Place.objects.get(id=self.place.id).longitude
            self.find_neighborhood_district()
        elif not self.neighborhood and not self.district:
            self.find_neighborhood_district()
        self.private_address = f"{self.city} - {self.district} - {self.neighborhood}"
        if self.car_model and not self.company:
            print(self.car_model.name)
            self.company = CarModel.objects.get(id=self.car_model.id).company
        super().save(*args, **kwargs)

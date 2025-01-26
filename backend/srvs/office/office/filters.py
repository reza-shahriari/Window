from random import choices

from backend.srvs.office.office.models import (
    Post,
    CarModel,
    Company,
    City,
)
import django_filters
from django_filters.fields import CSVWidget


class PostFilter(django_filters.FilterSet):
    color_id = django_filters.MultipleChoiceFilter(
        choices=Post.Color.choices,
        widget=CSVWidget,
    )
    gearbox_id = django_filters.MultipleChoiceFilter(
        choices = Post.Gearbox.choices,
        widget = CSVWidget
    )
    is_offroad = django_filters.BooleanFilter()
    price = django_filters.RangeFilter()
    rent_type_id = django_filters.MultipleChoiceFilter(
        choices = Post.RentType.choices,
        widget = CSVWidget,
    )
    rent = django_filters.RangeFilter()
    built_year = django_filters.RangeFilter()
    kilometer = django_filters.RangeFilter()
    car_model = django_filters.ModelMultipleChoiceFilter(
        queryset=CarModel.objects.all(),
        widget = CSVWidget,
    )
    company = django_filters.ModelMultipleChoiceFilter(
        queryset=Company.objects.all(),
        widget = CSVWidget,
    )
    city = django_filters.ModelMultipleChoiceFilter(
        queryset=City.objects.all(),
        widget = CSVWidget,
    )


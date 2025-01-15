from rest_framework import serializers

from backend.srvs.office.office.models import (
    Post,
    CarModel,
    Company,
)

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"

class CarModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField(
        read_only=True,
        allow_null=True,
        allow_empty=True,
    )
    city = serializers.StringRelatedField(
        read_only=True,
        allow_null=True,
        allow_empty=True,
    )
    district = serializers.StringRelatedField(
        read_only=True,
        allow_null=True,
        allow_empty=True,
    )
    private_address = serializers.ReadOnlyField(
        allow_null=True,
    )

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "color_id",
            "gearbox_id",
            "is_offroad",
            "price",
            "rent_type_id",
            "rent",
            "built_year",
            "kilometer",
            "description",
            "car_model",
            "company",
            "city",
            "district",
            "neighborhood",
            "public_address",
            "private_address",
            "latitude",
            "longitude",
            "place",
        ]

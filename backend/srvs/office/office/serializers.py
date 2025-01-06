from rest_framework import serializers

from backend.srvs.office.office.models import (
    Post,
    CarModel,
)

class CarModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarModel
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"

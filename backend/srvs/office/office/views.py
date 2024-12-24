from rest_framework.viewsets import ModelViewSet

from backend.srvs.office.office.models import (
    Post,
    CarModel,
)
from backend.srvs.office.office.serializers import (
    PostSerializer,
    CarModelSerializer,
)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CarModelViewSet(ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

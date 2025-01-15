from rest_framework.viewsets import ModelViewSet

from backend.srvs.office.office.models import (
    Post,
    CarModel,
    Company,
)
from backend.srvs.office.office.serializers import (
    PostSerializer,
    CarModelSerializer,
    CompanySerializer,
)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CarModelViewSet(ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

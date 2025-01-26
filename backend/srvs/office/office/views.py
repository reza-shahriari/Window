from rest_framework.viewsets import ModelViewSet

from backend.srvs.office.office.models import (
    Post,
    CarModel,
    Company,
)
from backend.srvs.office.office.permissions import ProtectedViewPermission
from backend.srvs.office.office.serializers import (
    PostSerializer,
    CarModelSerializer,
    CompanySerializer,
)
from backend.srvs.office.office.filters import PostFilter
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostFilter
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class CarModelViewSet(ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = [ProtectedViewPermission]

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

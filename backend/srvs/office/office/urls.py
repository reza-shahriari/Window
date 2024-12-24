from django.contrib import admin
from django.urls import (
    path,
    include,
)
from rest_framework import routers

from backend.srvs.office.office.views import (
    PostViewSet,
    CarModelViewSet,
)

office_router = routers.DefaultRouter()
office_router.register(r'posts', PostViewSet)
office_router.register(r"models", CarModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("office/", include(office_router.urls)),
]

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend.srvs.office.office.views import (
    PostViewSet,
    CarModelViewSet,
    CompanyViewSet,
    predict_image  # Add this import
)
from django.conf import settings
from django.conf.urls.static import static

from backend.srvs.office.gate import urls as gate_url

office_router = routers.DefaultRouter()
office_router.register(r'posts', PostViewSet)
office_router.register(r"models", CarModelViewSet)
office_router.register(r"companies", CompanyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("office/", include(office_router.urls)),
    path("", include(gate_url)),
    path('api/predict/', predict_image, name='predict-image'),  
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

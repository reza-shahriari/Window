from django.urls import (
    include,
    path,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

from backend.srvs.office.gate.views import UserViewSet, MyObtainTokenPairView

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    path("auth/", include(router.urls)),
    path('auth/login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

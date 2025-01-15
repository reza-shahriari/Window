import random
from datetime import datetime
import pytz
from rest_framework.viewsets import GenericViewSet
from backend.srvs.office.gate.serializers import UserSerializer, MyTokenObtainPairSerializer, iran_tz
from backend.srvs.office.gate.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_409_CONFLICT
from backend.srvs.office.gate.settings import (
    OTP_LOWER_LIMIT,
    OTP_UPPER_LIMIT,
)
from django.core.mail import send_mail
from django.conf import settings

iran_tz = pytz.timezone('Iran')

class UserViewSet(GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


    @action(detail=False, methods=['post'], url_path="send-otp")
    def send_otp(self, request, pk=None):
        _email = request.data.get('username', None)

        if _email:
            otp = str(random.randint(OTP_LOWER_LIMIT, OTP_UPPER_LIMIT))
            params = {
                'receptor': _email,
                'template': 'verify',
                'token': otp,
                'type': 'sms',
            }
            send_mail(
                "Email Verification",
                f"your password is {otp}",
                settings.EMAIL_HOST_USER,
                [_email],
                fail_silently=False,
            )
            if user := User.objects.filter(username=_email).first():
                user.set_password(otp)
                user.password_updated_at = datetime.now(tz=iran_tz)
                user.save()
            else:
                User.objects.create_user(
                    username=_email,
                    password=otp,
                    password_updated_at=datetime.now(tz=iran_tz),
                )
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_409_CONFLICT)


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

    class Meta:
        fields = "__all__"

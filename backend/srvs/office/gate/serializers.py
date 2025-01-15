from rest_framework import serializers
from backend.srvs.office.gate.models import User
from backend.srvs.office.office.exceptions import NeedLoginError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from datetime import datetime, timedelta
import pytz

iran_tz = pytz.timezone('Iran')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username",]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.get_username()
        token['groups'] = []
        for group in user.groups.all():
            token['groups'].append(group.name)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        two_minute_ago = datetime.now(tz=iran_tz) - timedelta(minutes=2)
        update_time = self.user.password_updated_at
        if not self.user.password_updated_at:
            raise NeedLoginError
        if update_time < two_minute_ago:
            raise NeedLoginError
        return data

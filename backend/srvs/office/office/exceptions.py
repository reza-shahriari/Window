from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_403_FORBIDDEN


class NeedLoginError(APIException):
    status_code = HTTP_403_FORBIDDEN
    default_detail = {'error': True, 'message': 'you need to login with new otp number'}
    default_code = 'not_authenticated'

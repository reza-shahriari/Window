from pathlib import Path
from environs import Env
import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
env = Env()
env.read_env()

SECRET_KEY = env.str("SECRET_KEY", defualt="django-insecure-^qh%5i!p0ytiqi=!yjdvv1vtopxc_2a^ed!u)#a529jic5&@de")
DEBUG = env.bool("DEBUG", default=True)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default="127.0.0.1,backend,0.0.0.0")


# default backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env.str("EMAIL_HOST", default="smtp.gmail.com")
EMAIL_PORT = env.str("EMAIL_PORT", default='587') # Recommended
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", default="windowprojectsoftware@gmail.com")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", default="kzrh biil kifa nfjn")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)  # Use EMAIL_PORT 587 for TLS
# EMAIL_USE_SSL = env.bool("EMAIL_USE_TLS", default=False)  # EUse MAIL_PORT 465 for SSL

ADMIN_USER_NAME=env.str("ADMIN_USER_NAME", default="admin")
ADMIN_USER_EMAIL=env.str("ADMIN_USER_EMAIL", default=None)


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'backend.srvs.office.office',
    'backend.srvs.office.gate',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.srvs.office.office.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.srvs.office.office.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

REST_FRAMEWORK = {
    # "DEFAULT_FILTER_BACKENDS": [
    #     "django_filters.rest_framework.DjangoFilterBackend",
    # ],
    "DEFAULT_PAGINATION_CLASS": (
        "rest_framework.pagination.LimitOffsetPagination"
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # 'DEFAULT_THROTTLE_CLASSES': [
    #     'rest_framework.throttling.AnonRateThrottle',
    #     'rest_framework.throttling.UserRateThrottle'
    # ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '60/minute',
    #     'user': '60/minute'
    # },
    "PAGE_SIZE": 10,
}

AUTH_USER_MODEL = 'gate.User'


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Iran"
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JWT_EXPIRE_DAYS = env.int("JWT_EXPIRE_DAYS", default=365)

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=JWT_EXPIRE_DAYS),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=JWT_EXPIRE_DAYS),
}

MANAGERS=[]
ADMINS=[]
if all([ADMIN_USER_NAME, ADMIN_USER_EMAIL]):
    ADMINS +=[
        (f'{ADMIN_USER_NAME}', f'{ADMIN_USER_EMAIL}')
    ]
    MANAGERS=ADMINS

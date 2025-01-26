from django.contrib import admin
from .models import (
    Post,
    Neighborhood,
    District,
    City,
)
from backend.srvs.office.gate.models import User
from django.contrib.auth.models import Permission, ContentType

admin.site.register(Post)
admin.site.register(User)
admin.site.register(Permission)
admin.site.register(ContentType)
admin.site.register(Neighborhood)
admin.site.register(District)
admin.site.register(City)

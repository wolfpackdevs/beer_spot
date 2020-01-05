from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from . import models


# Register your models here.
admin.site.register(models.Brewery)
admin.site.register(models.Brewer)
admin.site.register(models.Viewer)




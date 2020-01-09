from django.contrib import admin
from . import models

# Register your models here.


admin.site.register(models.Viewer)


admin.site.register(models.Preference)
from django.contrib import admin
from . import models


class StyleAdmin(admin.ModelAdmin):
    list_display = ['style']


admin.site.register(models.Style, StyleAdmin)


class FlavorAdmin(admin.ModelAdmin):
    list_display = ['flavor_note']


admin.site.register(models.Flavor, FlavorAdmin)


class GenericBeerAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(models.GenericBeer, GenericBeerAdmin)


class BeerAdmin(admin.ModelAdmin):
    list_display = ['name', 'brewery']


admin.site.register(models.Beer, BeerAdmin)

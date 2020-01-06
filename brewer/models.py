from django.db import models
from accounts.models import Brewery


class Style(models.Model):
    style = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.style}'

    def __repr__(self):
        return f'{self.style}'


class Flavor(models.Model):
    flavor_note = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.flavor_note}'

    def __repr__(self):
        return f'{self.flavor_note}'


class GenericBeer(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='g_beer/images/%Y/%m/%d', default='default/images/default.png',
                              null=True, blank=True)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    flavor = models.ManyToManyField(Flavor)
    abv = models.FloatField()


class Beer(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='beer/images/%Y/%m/%d', default='default/images/default.png',
                              null=True, blank=True)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE, related_name='brewery')
    style = models.ForeignKey(Style, on_delete=models.CASCADE, related_name='style_type')
    flavor = models.ManyToManyField(Flavor)
    abv = models.FloatField(blank=True)
    date_added = models.DateField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} by {self.brewery}'

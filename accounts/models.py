from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Brewery(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logos/images/%Y/%m/%d', default='default/images/default.png',
                             null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'


class Brewer(models.Model):
    is_brewer = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    brewery = models.OneToOneField(Brewery, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brewery},{self.user}'


class Viewer(models.Model):
    is_brewer = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profiles/images/%Y/%m/%d', default='default/images/default.png',
                                null=True, blank=True)

    def __repr__(self):
        return f"{self.user}"

    def __str__(self):
        return f"{self.user}"

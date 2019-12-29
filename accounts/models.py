from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Brewery(models.Model):
    name = models.CharField(max_length=200)

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

    def __repr__(self):
        return f"{self.user}"

    def __str__(self):
        return f"{self.user}"

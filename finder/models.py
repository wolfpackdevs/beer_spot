from django.db import models
from django.contrib.auth.models import User
from brewer.models import Beer


# Create your models here.

class Viewer(models.Model):
    first_use = models.BooleanField(default=True)
    is_brewer = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profiles/images/%Y/%m/%d', default='default.png',
                                null=True, blank=True)

    def __repr__(self):
        return f"{self.user}"

    def __str__(self):
        return f"{self.user}"


class Preference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_list')
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE, related_name='beer_liked')
    like = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}:{self.beer}:{self.like}'

    class Meta:
        unique_together = ('user', 'beer', 'like')


import django_filters
from brewer.models import Beer
from accounts.models import Brewery


class BeerFilter(django_filters.FilterSet):
    class Meta:
        model = Beer
        fields = ['style', 'flavor',]


class BreweryFilter(django_filters.FilterSet):
    class Meta:
        model = Brewery
        fields = ['name']

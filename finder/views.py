from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from . import filters
from accounts.models import Brewer
from brewer.models import GenericBeer, Beer, Brewery

from . import models


# Create your views here.

@login_required
def dashbord(request):
    if Brewer.objects.filter(user=request.user).exists():
        return redirect('brewer')
    return render(request, 'finder/dashbord.html')


@login_required
def tutorial_1(request):
    if Brewer.objects.filter(user=request.user).exists():
        return redirect('brewer')
    g_beer = GenericBeer.objects.all()
    return render(request, 'finder/tutorial_1.html', {'g_beer': g_beer})


@login_required
def tutorial_2(request, id):
    if Brewer.objects.filter(user=request.user).exists():
        return redirect('brewer')
    g_beer = GenericBeer.objects.get(id=id)
    beers_s = Beer.objects.filter(style=g_beer.style)
    beers_f = Beer.objects.filter(flavor__in=g_beer.flavor.all())
    return render(request, 'finder/tutorial_2.html', {'beers_s': beers_s,
                                                      'beers_f': beers_f})


@login_required
def beer_f_info(request,id):
    if Brewer.objects.filter(user=request.user).exists():
        return redirect('brewer')
    beer = Beer.objects.get(id=id)
    return render(request, 'finder/beer_f_info.html', {'beer': beer})


@login_required
def all_beers(request):
    if Brewer.objects.filter(user=request.user).exists():
        return redirect('brewer')
    brewerys = Brewery.objects.all().order_by('name')
    brewery_filter = filters.BreweryFilter(request.GET, queryset=brewerys)
    return render(request, 'finder/all_beers.html', {'filter': brewery_filter})


@login_required
def search_beers(request):
    beer_list = Beer.objects.all()
    beer_filter = filters.BeerFilter(request.GET, queryset=beer_list)
    return render(request, 'finder/search_beer.html', {'filter':beer_filter})


@login_required
def like_beer(request, id):
    if Brewer.objects.filter(user=request.user).exists():
        return redirect('brewer')
    beer = Beer.objects.get(id=id)
    if models.Preference.objects.filter(user=request.user, beer=beer).exists():
        messages.error(request, 'you already liked or disliked this beer')
        return redirect('beer_f_info', id=beer.id)
    else:
        user = request.user
        like = models.Preference(user=user, beer=beer)
        like.save()
        beer.likes += 1
        beer.save()
        return redirect('beer_f_info', id=beer.id)


@login_required
def dislike_beer(request, id):
    if Brewer.objects.filter(user=request.user).exists():
        return redirect('brewer')
    beer = Beer.objects.get(id=id)
    if models.Preference.objects.filter(user=request.user, beer=beer).exists():
        messages.error(request, 'you already liked or disliked this beer')
        return redirect('beer_f_info', id=beer.id)
    else:
        user = request.user
        like = models.Preference(user=user, beer=beer, like=False)
        like.save()
        beer.dislikes += 1
        beer.save()
        return redirect('beer_f_info', id=beer.id)

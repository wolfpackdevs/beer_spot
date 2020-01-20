from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from . import filters, decorators
from brewer.models import GenericBeer, Beer, Brewery

from . import models


# Create your views here.

@decorators.viewers_only
@login_required
def dashbord(request):
    user_pref = models.Preference.objects.filter(user=request.user, like=True).all()
    viewer = models.Viewer.objects.get(user=request.user)
    if viewer.first_use:
        viewer.first_use = False
        viewer.save()
        return redirect('tutorial_1')
    liked_beers_v = user_pref[:5]
    flavors_l = []
    beer_l = []
    for pref in user_pref:
        beer_l.append(pref.beer)
        for flavor in pref.beer.flavor.all():
            flavors_l.append(flavor)
    flavors_l = set(flavors_l)
    flavors_l_un = list(flavors_l)
    beer_r = Beer.objects.filter(flavor__in=flavors_l_un).distinct().order_by('-likes')
    beer_r = beer_r.exclude(id__in=[beer.id for beer in beer_l])[:5]
    viewer = models.Viewer.objects.get(user=request.user)
    return render(request, 'finder/dashbord.html', {'l_beer': liked_beers_v,
                                                    'beer_r': beer_r,
                                                    'viewer': viewer})


@login_required
@decorators.viewers_only
def all_liked_beer(request):
    user_pref = models.Preference.objects.filter(user=request.user, like=True).all()
    return render(request, 'finder/all_liked.html', {'user_pref': user_pref})


@login_required
@decorators.viewers_only
def all_rec_beer(request):
    user_pref = models.Preference.objects.filter(user=request.user, like=True).all()
    flavors_l = []
    beer_l = []
    for pref in user_pref:
        beer_l.append(pref.beer)
        for flavor in pref.beer.flavor.all():
            flavors_l.append(flavor)
    flavors_l = set(flavors_l)
    flavors_l_un = list(flavors_l)
    beer_r = Beer.objects.filter(flavor__in=flavors_l_un).distinct().order_by('-likes')
    beer_r = beer_r.exclude(id__in=[beer.id for beer in beer_l])
    return render(request, 'finder/all_rec.html', {'beer_r': beer_r})


@login_required
@decorators.viewers_only
def tutorial_1(request):
    g_beer = GenericBeer.objects.all()
    return render(request, 'finder/tutorial_1.html', {'g_beer': g_beer})


@login_required
@decorators.viewers_only
def tutorial_2(request, id):
    g_beer = GenericBeer.objects.get(id=id)
    beers_s = Beer.objects.filter(style=g_beer.style)
    beers_f = Beer.objects.filter(flavor__in=g_beer.flavor.all())
    return render(request, 'finder/tutorial_2.html', {'beers_s': beers_s,
                                                      'beers_f': beers_f})


@login_required
@decorators.viewers_only
def beer_f_info(request, id):
    beer = Beer.objects.get(id=id)
    return render(request, 'finder/beer_f_info.html', {'beer': beer})


@login_required
@decorators.viewers_only
def all_beers(request):
    brewerys = Brewery.objects.all().order_by('name')
    brewery_filter = filters.BreweryFilter(request.GET, queryset=brewerys)
    return render(request, 'finder/all_beers.html', {'filter': brewery_filter})


@login_required
@decorators.viewers_only
def search_beers(request):
    beer_list = Beer.objects.all()
    beer_filter = filters.BeerFilter(request.GET, queryset=beer_list)
    return render(request, 'finder/search_beer.html', {'filter': beer_filter})


@login_required
@decorators.viewers_only
def like_beer(request, id):
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
@decorators.viewers_only
def dislike_beer(request, id):
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

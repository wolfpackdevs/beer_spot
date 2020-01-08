from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from accounts.models import Brewer, Viewer
from brewer.models import GenericBeer, Beer, Brewery


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
    return render(request, 'finder/all_beers.html', {'brewerys': brewerys})

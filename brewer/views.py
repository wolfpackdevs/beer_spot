from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms, models
from accounts.models import Brewer


# Create your views here.


@login_required
def brewer_dashbord(request):
    brewer = Brewer.objects.get(user=request.user)
    return render(request, 'brewer/brewer.html', {'brewer': brewer})


@login_required
def add_beer(request):
    if request.method == 'POST':
        form = forms.AddBeerForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            style_new = form.cleaned_data['style']
            flavors_new = (form.cleaned_data['flavors']).split(',')
            flavors = []
            abv = form.cleaned_data['abv']
            brewer = Brewer.objects.get(user=request.user)
            brewery = brewer.brewery
            image = form.cleaned_data['image']
            style, created = models.Style.objects.get_or_create(style=style_new)
            for flavor in flavors_new:
                f_new, created = models.Flavor.objects.get_or_create(flavor_note=flavor)
                flavors.append(f_new)
            beer = models.Beer(name=name, image=image, brewery=brewery, style=style, abv=abv)
            beer.save()
            beer.flavor.add(*flavors)
            return redirect('brewer')
    else:
        form = forms.AddBeerForm()
    return render(request, 'brewer/add_beer.html', {'form': form})


@login_required
def brewer_beer(request):
    brewer = Brewer.objects.get(user=request.user)
    brewery = brewer.brewery
    beers = models.Beer.objects.filter(brewery=brewery).all()
    return render(request, 'brewer/brewers_beer.html', {'beers': beers, 'brewery': brewery})


@login_required
def beer_info(request, id):
    beer = models.Beer.objects.get(id=id)
    return render(request, 'brewer/beer_info.html', {'beer': beer})


@login_required
def change_beer(request, id):
    beer = models.Beer.objects.get(id=id)
    if request.method == 'POST':
        form = forms.ChangeBeerForm(request.POST, request.FILES, instance=beer)
        if form.is_valid():
            beer.style = form.cleaned_data['style']
            flavors = []
            flavors_new = (form.cleaned_data['flavor']).split(',')
            for flavor in flavors_new:
                f_new, created = models.Flavor.objects.get_or_create(flavor_note=flavor)
                flavors.append(f_new)
            beer.image = form.cleaned_data['image']
            beer.flavor.clear()
            beer.flavor.add(*flavors)
            beer.save()
            return redirect('brewers_beer')
    else:
        form = forms.ChangeBeerForm(instance=beer)
    return render(request, 'brewer/change_beer.html', {'beer': beer,
                                                       'form': form})

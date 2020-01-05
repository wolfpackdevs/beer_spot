from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms, models
from accounts.models import Brewer, Viewer


# Create your views here.


@login_required
def dashbord(request):
    if Brewer.objects.filter(user=request.user).exists():
        return redirect('brewer')
    return render(request, 'finder/dashbord.html')


@login_required
def brewer_dashbord(request):
    brewer = Brewer.objects.get(user=request.user)
    return render(request, 'finder/brewer.html', {'brewer': brewer})


@login_required
def add_beer(request):
    if request.method == 'POST':
        form = forms.AddBeerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            style_new = form.cleaned_data['style']
            flavors_new = (form.cleaned_data['flavors']).split(',')
            flavors = []
            abv = form.cleaned_data['abv']
            brewer = Brewer.objects.get(user=request.user)
            brewery = brewer.brewery
            style, created = models.Style.objects.get_or_create(style=style_new)
            for flavor in flavors_new:
                f_new, created = models.Flavor.objects.get_or_create(flavor_note=flavor)
                flavors.append(f_new)
            beer = models.Beer(name=name, brewery=brewery, style=style, abv=abv)
            beer.save()
            beer.flavor.add(*flavors)
    else:
        form = forms.AddBeerForm()
    return render(request, 'finder/add_beer.html', {'form': form})

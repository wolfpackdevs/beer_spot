from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from . import forms, models


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_psw = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_psw)
            viewer = models.Viewer(user=user)
            viewer.save()
            login(request, user)
            return redirect('dashbord')
    else:
        form = forms.SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def signup_brewer(request):
    if request.method == 'POST':
        form = forms.SignUpBrewerForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            raw_psw = form.cleaned_data['password1']
            brewery = models.Brewery(name=form.cleaned_data['brewery_name'])
            brewery.save()
            user_new = User(username=username, email=email, password=raw_psw)
            user = authenticate(username=username, password=raw_psw)
            brewer = models.Brewer(user=user, brewery=brewery)
            brewer.save()
            login(request, user)
            return redirect('dashbord')
    else:
        form = forms.SignUpBrewerForm()
    return render(request, 'accounts/signup_brewer.html', {'form': form})

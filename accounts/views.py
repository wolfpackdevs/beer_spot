from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from . import forms, models
from finder.models import Viewer
from finder.decorators import viewers_only


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_psw = form.cleaned_data['password1']
            picture = form.cleaned_data['picture']
            print(picture)
            user = authenticate(username=username, password=raw_psw)
            viewer = Viewer(user=user, picture=picture)
            viewer.save()
            login(request, user)
            return redirect('dashbord')
    else:
        form = forms.SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def signup_brewer(request):
    if request.method == 'POST':
        form = forms.SignUpBrewerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            raw_psw = form.cleaned_data['password1']
            logo = form.cleaned_data['logo']
            brewery = models.Brewery(name=form.cleaned_data['brewery_name'],
                                     logo=logo)
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


@login_required
def edit_brewery(request):
    brewer = models.Brewer.objects.get(user=request.user)
    brewery = brewer.brewery
    if request.method == 'POST':
        form = forms.EditBrewery(request.POST, request.FILES, instance=brewery)
        if form.is_valid():
            form.save()
        return redirect('brewer')
    else:
        form = forms.EditBrewery(instance=brewery)
    return render(request, 'accounts/edit_brewery.html', {'form': form})


@login_required
def edit_brewer(request):
    if request.method == 'POST':
        form = forms.EditBrewer(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'username was changed to {request.user.username}')
        else:
            messages.error(request, 'please try again')
    else:
        form = forms.EditBrewer(instance=request.user)
    return render(request, 'accounts/edit_brewer.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was changed')
        else:
            messages.error(request, 'please try again')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})


@login_required
@viewers_only
def edit_viewer(request):
    if request.method == 'POST':
        form = forms.EditViewerInfo(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'your information has been updated')
    else:
        form = forms.EditViewerInfo(instance=request.user)
    return render(request, 'accounts/edit_viewer.html', {'form': form})


@login_required
@viewers_only
def change_viewer_pic(request):
    viewer = Viewer.objects.get(user=request.user)
    if request.method == 'POST':
        form = forms.EditViewerPic(request.POST, request.FILES, instance=viewer)
        if form.is_valid():
            form.save()
            return redirect('dashbord')
    else:
        form = forms.EditViewerPic(instance=viewer)
    return render(request, 'accounts/edit_viewer_pic.html', {'form': form})

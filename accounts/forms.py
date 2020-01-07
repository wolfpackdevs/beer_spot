from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from . import models


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    picture = forms.ImageField(required=False,
                               widget=(forms.FileInput(attrs={'class': 'form-control'})))
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=254, help_text='Required',
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(help_text=password_validation.password_validators_help_text_html(),
                                label='Set password'
                                , widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'picture', 'first_name', 'last_name', 'email', 'password1', 'password2')


class SignUpBrewerForm(UserCreationForm):
    brewery_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=256, help_text='required',
                             widget=forms.EmailInput())
    logo = forms.ImageField(required=False,
                            widget=(forms.FileInput(attrs={'class': 'form-control'})))

    class Meta:
        model = User
        fields = ('username', 'brewery_name', 'logo', 'email', 'password1', 'password2')


class EditBrewery(forms.ModelForm):
    class Meta:
        model = models.Brewery
        fields = ('name', 'logo')


class EditBrewer(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')



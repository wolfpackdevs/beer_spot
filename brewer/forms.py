from django import forms
from . import models


class AddBeerForm(forms.Form):
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    style = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    flavors = forms.CharField(max_length=400, help_text='place comma after each flavor type',
                              widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    abv = forms.FloatField(min_value=0, label='Alcohol by Volume',
                           widget=forms.NumberInput(attrs={'class': 'form-control'}))


class ChangeBeerForm(forms.ModelForm):
    # style = forms.CharField(max_length=100,
    #                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    flavor = forms.CharField(max_length=400, help_text='place comma after each flavor type',
                             widget=forms.Textarea(attrs={'class': 'form-control'}))
    abv = forms.FloatField(min_value=0, label='Alcohol by Volume',
                           widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Beer
        fields = ['style', 'flavor', 'image', 'abv', 'is_available']
        widgets = {'is_available': forms.CheckboxInput(),
                   'style': forms.Select(attrs={'class': 'form-control'})}

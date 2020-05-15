from django import forms
from . import models


class AddBeerForm(forms.Form):
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    style = forms.ModelChoiceField(queryset=models.Style.objects.all().order_by('style'))
    flavors = forms.CharField(max_length=400, help_text='place comma after each flavor type',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    abv = forms.FloatField(min_value=0, label='Alcohol by Volume',
                           widget=forms.NumberInput(attrs={'class': 'form-control'}))
    message = forms.CharField(required=False,
                              widget=forms.Textarea(attrs={'class': 'form-control'}))


class ChangeBeerForm(forms.ModelForm):
    flavor = forms.CharField(max_length=400, help_text='place comma after each flavor type',
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    abv = forms.FloatField(min_value=0, label='Alcohol by Volume',
                           widget=forms.NumberInput(attrs={'class': 'form-control'}))
    message = forms.CharField(required=False,
                              widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Beer
        fields = ['style', 'flavor', 'image', 'abv', 'is_available', 'message']
        widgets = {'is_available': forms.CheckboxInput(),
                   'style': forms.Select(attrs={'class': 'form-control'})
                   }


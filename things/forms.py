"""Forms of the project."""
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class ThingForm(forms.Form):
    name=forms.CharField()
    description=forms.Textarea()
    quantity = forms.IntegerField()
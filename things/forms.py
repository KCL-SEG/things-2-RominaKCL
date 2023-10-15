"""Forms of the project."""
from django import forms
from .models import Thing


class ThingForm(forms.ModelForm):
    description = forms.Textarea()
    quantity = forms.NumberInput()

    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']

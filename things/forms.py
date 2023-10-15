"""Forms of the project."""
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class ThingForm(forms.Form):
    name=forms.CharField(max_length=35)
    description=forms.Textarea(max_length=120)
    quantity = forms.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(50)
        ]
    )
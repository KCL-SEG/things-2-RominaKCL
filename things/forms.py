"""Forms of the project."""
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class ThingForm(forms.Form):
    name=forms.CharField(max_length=35, unique=True, blank=False)
    description=forms.Textarea(max_length=120, blank=True, unique=False)
    quantity = forms.IntegerField(
        unique=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(50)
        ]
    )
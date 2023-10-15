"""Forms of the project."""
from django import forms
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator

class ThingForm(forms.Form):
    name=forms.CharField(max_length=35)
    description=forms.Textarea()
    quantity=forms.NumberInput(
        validators=[
            MinLengthValidator(0),
            MaxLengthValidator(51),
        ]
    )
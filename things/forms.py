"""Forms of the project."""
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class ThingForm(forms.Form):
    name = forms.CharField(label='name',max_length=35)
    description = forms.CharField(label='description',widget=forms.Textarea, max_length=120)
    quantity= forms.IntegerField(widget=forms.NumberInput, label='quantity', validators=[MinValueValidator(0), MaxValueValidator(50)])

from django import forms
from .models import Item

class FilterForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'price']
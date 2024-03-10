# forms.py
from django import forms
from .models import FormData

class SearchForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = ['from_field', 'to_field', 'date']
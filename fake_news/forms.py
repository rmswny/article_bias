from django import forms
from .models import Publisher

class FormName(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['article_address',]

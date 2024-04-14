from django.core import validators
from django import forms
from .models import Product

class ProductRegistration(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','image','price']
        widgets =  {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
        }
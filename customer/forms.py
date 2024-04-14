from django import forms
from .models import OrderModel, Contact

class OrderModel(forms.ModelForm):
  class Meta:
    model = OrderModel
    # fields = ["name", "email", "street", "city", "state", "zip_code"]
    fields = '__all__'
    labels = {'name': "name", "email": "email", "street": "street", "city": "city", "state": "state", "zip_code": "zip_code"}

class Contact(forms.ModelForm):
  class Meta:
    model = Contact
    fields = ['name','email','description']
    labels = {'name': "name", "email": "email","description":"description"}
from django.db import models
from state.models import *

class Product(models.Model):
    name = models.TextField(max_length=100)
    price = models.TextField(max_length=50)
    description = models.TextField(max_length=500, null=True)
    image = models.ImageField(upload_to='static/images', null=True, blank=True) #upload_to='prod_images/'
    category = models.TextField(max_length=100, null=True)
    stock = models.TextField(max_length=50, null=True)
    # category = models.ManyToManyField('Category', related_name='Item')

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.TextField(max_length=100)
    rid = models.TextField(max_length=50)
    email = models.EmailField(max_length = 254)
    mobile = models.IntegerField()

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.TextField(max_length=100)
    stid = models.TextField(max_length=50)
    address = models.TextField(max_length=100)
    mobile = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
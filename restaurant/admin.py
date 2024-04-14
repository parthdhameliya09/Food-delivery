from django.contrib import admin
from .models import Restaurant, Store, Product

# @admin.register(Product)
# class VendorProduct(admin.ModelAdmin):
#     list_display = ('name','description','image','price')

@admin.register(Restaurant)
class Restaurant(admin.ModelAdmin):
    list_display = ('rid','name','email','mobile')

@admin.register(Store)
class Store(admin.ModelAdmin):
    list_display = ('stid','name','restaurant','address','mobile')

# admin.site.register(Product)
# admin.site.register(Category)
# admin.site.register(Order)
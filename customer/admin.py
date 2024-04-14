from django.contrib import admin
from .models import MenuItem, Category, OrderModel, Contact

# admin.site.register(MenuItem)
admin.site.register(Category)
# admin.site.register(OrderModel)
@admin.register(MenuItem)
class MenuItem(admin.ModelAdmin):
    list_display = ('name','image','price')

@admin.register(OrderModel)
class OrderModel(admin.ModelAdmin):
    list_display = ('name','email','price','city','is_paid')

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('name','email','description')
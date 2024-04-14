from django.contrib import admin
from .models import State, City, Area

@admin.register(State)
class State(admin.ModelAdmin):
    list_display = ('sid','name')

@admin.register(City)
class City(admin.ModelAdmin):
    list_display = ('cid','name','state')

@admin.register(Area)
class Area(admin.ModelAdmin):
    list_display = ('aid','name','pincode','city','state')
from django.contrib import admin
from userauths.models import User, Vendor

class UserAdmin(admin.ModelAdmin):
      list_display = ['username', 'email']  

admin.site.register(User, UserAdmin)
admin.site.register(Vendor, UserAdmin)
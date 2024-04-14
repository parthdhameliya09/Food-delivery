from django.urls import path
from customer.views import Index, success, Invoice, save_pdf, Contact

app_name = "customer"

urlpatterns = [
    path('', index, name="index"),
    path('home/', views.Home, name='home'),
    path('contact/', views.Contact, name='contact'),
    path('submit/', views.submit, name='submit'),
    path('success/', success, name='success'),
    path('', save_pdf, name='test-view'),
    path('invoice/', Invoice, name='invoice'),
    path('add', views.ADD, name='add'),
    # path('submit/', OrderConfirmation.as_view(), name="submit"),
]

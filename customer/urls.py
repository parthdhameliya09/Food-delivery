from django.urls import path
from customer.views import Index

app_name = "customer"

urlpatterns = [
    path("", Index, nmae="index"),
    path('submit/', views.submit, name='submit'),
]

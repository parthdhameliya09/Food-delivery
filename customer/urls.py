from django.urls import path
from customer.views import Index

app_name = "customer"

urlpatterns = [
    path("", Index, name="index"),
    path('submit/', views.submit, name='submit'),
    # path('submit/', OrderConfirmation.as_view(), name="submit"),
]

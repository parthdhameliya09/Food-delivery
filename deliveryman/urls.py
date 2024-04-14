from django.urls import path
from .views import Dashboard, OrderDetails

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('order/', OrderDetails.as_view(), name='order-details')
]
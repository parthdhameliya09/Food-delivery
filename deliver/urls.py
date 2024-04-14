"""
URL configuration for deliver project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from restaurant import views
from customer.views import Index, About, contact, Order, OrderConfirmation, OrderPayConfirmation, ADD, Menu, MenuSearch, Checkout, Formdetail, LoginPage, SignupPage, Home, Logout, ForgotPwd, ChangePwd, Invoice, MyOrder, MyProfile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('restaurant/', include('restaurant.urls')),
    path('deliveryman/', include('deliveryman.urls')),
    path('',Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('contact/', contact.as_view(), name='contact'),
    path('myorder/', MyOrder.as_view(), name='myorder'),
    path('myprofile/', MyProfile.as_view(), name='myprofile'),
    path('invoice/', Invoice.as_view(), name='invoice'),
    path('signup/', SignupPage.as_view(), name='signup'),
    path('login/', LoginPage.as_view(), name='login'),
    path('forgotpwd/', ForgotPwd.as_view(), name='forgotpwd'),
    path('changepwd/<token>/', ChangePwd.as_view(), name='changepwd'),
    path('home/', Home.as_view(), name='home'),
    path('logout/', Logout.as_view(), name='logout'),
    path('menu/', Menu.as_view(), name='menu'),
    path('menu/search/', MenuSearch.as_view(), name='menu-search'),
    path('addproduct/', views.add_show, name='addandshow'),
    path('<int:id>/', views.update_data, name='updatedata'),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),
    path('order/', Order.as_view(), name = 'order'),
    path('Form_details/', Formdetail.as_view(), name = 'Form_details'),
    path('order-confirmation/<int:pk>', OrderConfirmation.as_view(), name='order-confirmation'),
    path('payment-confirmation/', OrderPayConfirmation.as_view(), name='payment-confirmation'),
    path('checkout/', Checkout.as_view(), name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

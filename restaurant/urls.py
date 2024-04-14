from django.urls import path
from .views import Dashboard, OrderDetails, update_data, SignupPage, LoginPage, ForgotPwd, ChangePwd

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    # path('', views.add_show, name='addandshow'),
    path('orders/<int:pk>/', OrderDetails.as_view(), name='order-details'),
    path('signup/', SignupPage.as_view(), name='signup'),
    path('login/', LoginPage.as_view(), name='login'),
    path('forgotpwd/', ForgotPwd.as_view(), name='forgotpwd'),
    path('changepwd/<token>/', ChangePwd.as_view(), name='changepwd'),
    # path('edit/<int:id>/', views.update_data, name='updatedata'),
    # path('delete/<int:id>/', views.delete_data, name='deletedata'),
]
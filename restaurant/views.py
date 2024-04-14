from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import datetime
from customer.models import OrderModel
from .forms import ProductRegistration
from .models import Product
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .helpers import send_forgot_password_mail
import uuid

# This Function will Display
def index(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'restaurant/dashboard.html', context)

# This Function will Add
def add_show(request):
    if request.method == 'POST':
        product = Product()
        product.name=request.POST.get('name')
        product.description=request.POST.get('description')
        product.price=request.POST.get('price')
        product.category=request.POST.get('category')
        product.stock=request.POST.get('stock')

        if len(request.FILES) != 0:
            product.image = request.FILES['image']

        product.save()
        messages.success(request, "Product added Successfully")
    product = Product.objects.all()
    return render(request, 'restaurant/dashboard.html', context={'pro':product})

# This Function will Update
def update_data(request, id):
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        fm = ProductRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Product Updated Successfully")
    return render(request, '', {'id':id})

# This Function will Delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        pi.delete()
        messages.success(request, "Product Deleted Successfully")
    return HttpResponseRedirect('/')

class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        # get the current date
        today = datetime.today()
        orders = OrderModel.objects.filter(created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)

        # loop through the orders and add the price value, check if order is not shipped
        unshhipped_orders = []
        total_revenue = 0
        for order in orders:
            total_revenue += order.price

            if not order.is_shipped:
                unshhipped_orders.append(order)

        # pass total no of orders and total revenue into template
        context = {
            'orders' : unshhipped_orders,
            'total_revenue' : total_revenue,
            'total_orders' : len(orders)
        }

        return render(request, 'restaurant/dashboard.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()

class OrderDetails(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        context = {
            'order' : order
        }
        return render(request, 'restaurant/order-details.html', context)

    def post(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        order.is_shipped = True
        order.save()

        context = {
            'order' : order
        }
        return render(request, 'restaurant/order-details.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()

class ForgotPwd(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'restaurant/forgotpwd.html')
    
    def post(self, request, *args, **kwargs):
        try:
            username = request.POST.get('username')

            if not User.objects.filter(username=username).first():
                messages.success(request, 'No user found with this username.')
                return redirect('/forgotpwd')
            user_obj = User.objects.get(username=username)
            token = str(uuid.uuid4())
            send_forgot_password_mail(user_obj, token)
            messages.success(request, 'An email is sent please check it.!')
            return redirect('/forgotpwd')

        except Exception as e:
            print(e)

        return render(request, 'restaurant/forgotpwd.html')

class ChangePwd(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'restaurant/changepwd.html')
    
    def post(self, request, *args, **kwargs):
        try:
            profile_obj = Profile.objects.get(forgot_password_token = token)
            print(profile_obj)            
        except Exception as e:
            print(e)
        return render(request, 'restaurant/changepwd.html')

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'restaurant/addproduct.html')

class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

class LoginPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'restaurant/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('addproduct')
        else:
            return HttpResponse("Username or Password is incorrect.!!")

        return render(request, 'restaurant/login.html')

class SignupPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'restaurant/signup.html')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            uname = request.POST.get('username')
            email = request.POST.get('email')
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')

            if pass1 != pass2:
                return HttpResponse("Your password and confirm password are not same!")
            else:
                my_user = User.objects.create_user(uname,email,pass1)
                my_user.save()
                return redirect('login')
        return render(request, 'restaurant/signup.html')
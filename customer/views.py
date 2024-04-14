import json
import razorpay
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import MenuItem, Category, OrderModel, Contact
from django.views.decorators.csrf import csrf_exempt
from deliver.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
from .helpers import send_forgot_password_mail
import uuid

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def index(request):
    if request.method == "POST":
        order_amount: 50000
        order_currency: "INR"
        client = razorpay.Client(
            auth=('rzp_test_Lq0WdpfE9BUb0t','lQ2MZLMuqQYhOv2WKVuXxZWX'))

        payment_order = client.order.create(dict(amount=order_amount, currency=order_currency, payment_capture=1))
        payment_order_id = payment_order['id']
        context = {
            'amount' : 500, 'api_key' : RAZORPAY_API_KEY, 'order_id' : payment_order_id
    }
    return render(request, 'customer/order-confirmation.html', context)

@csrf_exempt
def success(request):
        return render(request, 'success.html')

def ADD(request):
    return render(request, 'index.html')

# @login_required(login_url='login')
# def index(request):
#     return render(request,'index.html')

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

class MyOrder(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/myorder.html')

class MyProfile(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/myprofile.html')
        
class Invoice(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/invoice.html')

class contact(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/contact.html')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            description = request.POST['description']

            ins = Contact(name=name,email=email,description=description)
            ins.save()
            return redirect('/')
        return render(request, 'customer/contact.html')

# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         description = request.POST.get('description')
#         print(name,email,description)
#         # em = Contact(name=name,email=email,description=description)
#         # em.save()
#         return redirect('/')
#     return render(request, 'customer/contact.html')

class ForgotPwd(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/forgotpwd.html')
    
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

        return render(request, 'customer/forgotpwd.html')

class ChangePwd(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/changepwd.html')
    
    def post(self, request, *args, **kwargs):
        try:
            profile_obj = Profile.objects.get(forgot_password_token = token)
            print(profile_obj)            
        except Exception as e:
            print(e)
        return render(request, 'customer/changepwd.html')

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/home.html')

class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

class LoginPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect.!!")

        return render(request, 'customer/login.html')

class SignupPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/signup.html')

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
        return render(request, 'customer/signup.html')

class Order(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        # appetizers = MenuItem.objects.filter(category__name__contains='Appetizer')
        Bestseller = MenuItem.objects.filter(category__name__contains='Bestseller')
        Burger = MenuItem.objects.filter(category__name__contains='Burger')
        Pizza = MenuItem.objects.filter(category__name__contains='Pizza')
        Beverages = MenuItem.objects.filter(category__name__contains='Beverages')
        Dessert = MenuItem.objects.filter(category__name__contains='Dessert')
        Sides = MenuItem.objects.filter(category__name__contains='Sides')

        #pass into context
        context = {
            # 'appetizers': appetizers,
            'Bestseller':Bestseller,
            'Burger': Burger,
            'Pizza': Pizza,
            'Beverages': Beverages,
            'Dessert': Dessert,
            'Sides': Sides,
        }

        #render the template
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            fm = OrderModel(request.POST)
            if fm.is_valid():
                fm.save()
            price = request.POST.get('price'),
            items = request.POST.get('items'),
            street = request.POST.get('street')
            city = request.POST.get('city')
            state = request.POST.get('state')
            zip_code = request.POST.get('zip')

        order = OrderModel(
            price = price,
            items = items
        )
        order.save()
        
        return redirect('order-confirmation', pk=order.pk)

# class Order(View):
#     def get(self, request, *args, **kwargs):
#         #get every item from each category
#         # appetizers = MenuItem.objects.filter(category__name__contains='Appetizer')
#         Bestseller = MenuItem.objects.filter(category__name__contains='Bestseller')
#         Burger = MenuItem.objects.filter(category__name__contains='Burger')
#         Pizza = MenuItem.objects.filter(category__name__contains='Pizza')
#         Beverages = MenuItem.objects.filter(category__name__contains='Beverages')
#         Dessert = MenuItem.objects.filter(category__name__contains='Dessert')
#         Sides = MenuItem.objects.filter(category__name__contains='Sides')

#         #pass into context
#         context = {
#             # 'appetizers': appetizers,
#             'Bestseller':Bestseller,
#             'Burger': Burger,
#             'Pizza': Pizza,
#             'Beverages': Beverages,
#             'Dessert': Dessert,
#             'Sides': Sides,
#         }

#         #render the template
#         return render(request, 'customer/order.html', context)

#     def post(self, request, *args, **kwargs):
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         street = request.POST.get('street')
#         city = request.POST.get('city')
#         state = request.POST.get('state')
#         zip_code = request.POST.get('zip')

#         order_items = {
#             'items': []
#         }

#         items = request.POST.getlist('items[]')

#         for item in items:
#             menu_item = MenuItem.objects.get(pk__contains=int(item))
#             item_data = {
#                 'id': menu_item.pk,
#                 'name': menu_item.name,
#                 'price': menu_item.price
#             }

#             order_items['items'].append(item_data)

#             price = 0
#             item_ids = []

#         for item in order_items['items']:
#             price += item['price']
#             item_ids.append(item['id'])

#         order = OrderModel.objects.create(
#             price=price,
#             name=name,
#             email=email,
#             street=street,
#             city=city,
#             state=state,
#             zip_code=zip_code
#         )
#         order.items.add(*item_ids)

#         # After everything is done, send confirmation email to user
#         body = ('Thank you for your order! Your food is being made and will be delivered soon!\n'
#             f'Your total: {price}\n'
#             'Thank you again for your order!')

#         send_mail(
#             'Thank You For Your Order!',
#             body,
#             'example@example.com',
#             [email],
#             fail_silently=False
#         )

#         context = {
#             'item': order_items['items'],
#             'price': price
#         }

#         return redirect('order-confirmation', pk=order.pk)

class Formdetail(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/Form_details.html')

    def my_form(request):
        if request.method == "POST":
            form = OrderModel(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = OrderModel()
        return render(request, 'Form_details.html', {'form': form})

class OrderConfirmation(View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)

        context = {
            'pk' : order.pk,
            'items' : order.items,
            'price' : order.price,
        }

        return render(request, 'customer/order_confirmation.html', context)

    def post(self, request, pk, *args, **kwargs):
        data = json.loads(request.body)

        if data['isPaid']:
            order = OrderModel.objects.get(pk=pk)
            order.is_paid = True
            order.save()
        return redirect('payment-confirmation')

class OrderPayConfirmation(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/order_pay_confirmation.html')

class Checkout(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/checkout.html')

class Menu(View):
    def get(self, request, *args, **kwargs):
        menu_items = MenuItem.objects.all()
        context = {
            'menu_items' : menu_items
        }
        return render(request, 'customer/menu.html', context)

class MenuSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")

        menu_items = MenuItem.objects.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query) |
            Q(description__icontains=query)
        )

        context = {
            'menu_items' : menu_items
        }
        return render(request, 'customer/menu.html', context)
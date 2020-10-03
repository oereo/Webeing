from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView

from order.models import OrderItem, Order
from .forms import UserCreationForm
from .models import User


class UserRegistrationView(CreateView):
    model = User  # 자동생성 폼에서 사용할 모델
    fields = ('email', 'phone_number', 'nickname', 'password')  # 자동생성 폼에서 사용할 필드


def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            # return render(request, 'shop/list.html')
            return redirect('/main/')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def signup_customer(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password_confirm']:
            user = User.objects.create_user(
                # request.POST['email'],
                phone_number=request.POST['phonenumber'],
                password=request.POST['password'],
                email=request.POST['username'],
                nickname=request.POST['nickname'],
                date_of_birth=request.POST['dateofbirth'],
            )
            auth.login(request, user)

        return redirect('/main/')

    else:
        form = UserCreationForm()
    return render(request, 'signupcustomer.html', {'form': form})


def signup_seller(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password_confirm']:
            user = User.objects.create_seller(
                # request.POST['email'],
                phone_number=request.POST['phonenumber'],
                password=request.POST['password'],
                email=request.POST['username'],
                nickname=request.POST['nickname'],
                date_of_birth=request.POST['dateofbirth'],
                seller_address=request.POST['seller_address'],
                business_number=request.POST['business_number'],
                seller_name=request.POST['seller_name'],
            )
            auth.login(request, user)

<<<<<<< HEAD
        return redirect('sellerPage')
        
=======

        return redirect('/main/')



>>>>>>> 2bad7f8a14aaf9731b16dedc88398c1dceeab3d2
    else:
        form = UserCreationForm()
    return render(request, 'signupseller.html', {'form': form})


def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        print('log out success')
        return redirect('/main/')
    return render(request, 'shop/list.html')


def customer_page(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    order_items_list = []

    for order in orders:
        order_items_list.append(OrderItem.objects.filter(order=order))
    # orderitems = OrderItem.objects.filter(order=order[0])
    # orderitems = get_object_or_404(Order, pk=order_id)
    # orderitems = Order.objects.values('user', 'OrderItem__created')
    # orderitems = Order.objects.filter(user=user).select_related('user')
    return render(request, 'customerPage.html', {'order_items_list': order_items_list, 'orders': orders})
    # return render(request, 'customerPage.html')

def seller_page(request):
    return render(request, 'sellerPage.html')


def signup(request):
    return render(request, 'signup.html')


def tos(request):
    return render(request, 'TOS.html')


def tos_user(request):
    return render(request, 'TOS_user.html')

from django.shortcuts import render, redirect
from django.contrib import auth
#from django.contrib.auth.models import User
from django.contrib.auth import models, views, login
from .forms import UserCreationForm
from django.views.generic import CreateView
from .models import User


class UserRegistrationView(CreateView):
    model = User                            # 자동생성 폼에서 사용할 모델
    fields = ('email', 'phone_number', 'nickname','password')  # 자동생성 폼에서 사용할 필드

def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email = email, password = password)
        if user is not None:
            auth.login(request, user)
            return render(request,'shop/list.html')

        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def signup_customer(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password_confirm']:
            user = User.objects.create_user(
                # request.POST['email'],
                phone_number = request.POST['phonenumber'],
                password = request.POST['password'],
                email = request.POST['username'],
                nickname = request.POST['nickname'],
                date_of_birth = request.POST['dateofbirth'],
            )
            auth.login(request, user)

        return redirect('home')
        
    else:
        form = UserCreationForm()
    return render(request, 'signupcustomer.html', {'form': form})

def signup_seller(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password_confirm']:
            user = User.objects.create_seller(
                # request.POST['email'],
                phone_number = request.POST['phonenumber'],
                password = request.POST['password'],
                email = request.POST['username'],
                nickname = request.POST['nickname'],
                date_of_birth = request.POST['dateofbirth'],
                seller_address = request.POST['seller_address'],
                business_number = request.POST['business_number'],
                seller_name = request.POST['seller_name'],
            )
            auth.login(request, user)

        return redirect('home')
        
    else:
        form = UserCreationForm()
    return render(request, 'signupseller.html', {'form': form})

def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        print('log out success')
        return render(request,'shop/list.html')
    return render(request,'shop/list.html')


def customerPage(request):
    return render(request, 'customerPage.html')

def sellerPage(request): # 사장님 페이지 
    user = request.user

    return render(request, 'sellerPage.html')

def signup(request):
    return render(request, 'signup.html')


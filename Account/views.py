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
            return redirect('home')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def signup(request):
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
            # user.is_active = False
            # user.save()        

        # form = UserCreationForm(request.POST)
        # if form.is_valid():
            #new_user = models.User.objects.create_user(**form.cleaned_data)
            #user = form.save(commit=False)
            #user.email = UserCreationForm.cleaned_data['email']
            # user.
            #user.save()
            #login(request, new_user)
            #auth.login(request, user)
        return redirect('home')
        
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        print('log out success')
        return redirect('/')
    return render(request,'home.html')
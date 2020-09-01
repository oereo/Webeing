from django.shortcuts import render, redirect
from django.contrib import auth
#from django.contrib.auth.models import User
from django.contrib.auth import models, views
from .forms import UserCreationForm
from django.views.generic import CreateView
from .models import User


class UserRegistrationView(CreateView):
    model = User                            # 자동생성 폼에서 사용할 모델
    fields = ('email', 'phone_number', 'nickname','password')  # 자동생성 폼에서 사용할 필드

def login(request):
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            #user.email = UserCreationForm.cleaned_data['email']
            # user.
            user.save()
            #auth.login(request, user)
            return redirect('home')
        else:
            return redirect('signup')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        print('log out success')
        return redirect('/')
    return render(request,'home.html')
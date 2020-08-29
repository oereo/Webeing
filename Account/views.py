from django.shortcuts import render, redirect
from django.contrib import auth

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        print('log out success')
        return redirect('/')
    return render(request,'home.html')
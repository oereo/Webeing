from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def landingPage(request):
    return render(request, 'landingPage.html')

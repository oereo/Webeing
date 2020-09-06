from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def japan(request):
    return render(request, 'japan.html')

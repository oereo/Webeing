from django.conf.urls import url
from django.urls import path, include
from mainPage import views

urlpatterns = [
    path('main/', views.home, name ="home"),
    path('japan/', views.japan, name ="japan"),

]
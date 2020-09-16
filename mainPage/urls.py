from django.conf.urls import url
from django.urls import path, include
from mainPage import views

urlpatterns = [
    path('main/', views.home, name ="home"),
    path('', views.landingPage, name="langdingPage"),

]
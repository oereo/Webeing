from django.conf.urls import url
from django.urls import path, include
from mainPage import views

urlpatterns = [
    path('', views.home, name ="home"),
]
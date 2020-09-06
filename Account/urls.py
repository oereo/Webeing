from django.conf.urls import url
from django.urls import path, include
from Account import views

urlpatterns = [
    path('logout/', views.logout, name ="logout"),
    path('login/', views.login_user, name = "login"),
    path('signupcustomer/', views.signup, name = "signup"),
    path('signupseller/', views.signup_seller, name = "signup_seller"),
    path('customerPage/', views.customerPage, name = "customerPage"),
    path('sellerPage/', views.sellerPage, name = "sellerPage"),

    #path('join/', views.UserRegistrationView.as_view(), name='join'),
]
from django.urls import path, include
from Account import views

urlpatterns = [
    path('logout/', views.logout, name="logout"),
    path('login/', views.login_user, name="login"),
    path('signup/', views.signup, name="signup"),

    path('signupcustomer/', views.signup_customer, name="signup_customer"),
    path('signupseller/', views.signup_seller, name="signup_seller"),
    path('customerPage/', views.customerPage, name="customerPage"),
    path('sellerPage/', views.sellerPage, name="sellerPage"),
    path('tos/', views.tos, name="tos")
]

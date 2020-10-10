from django.urls import path, include
from . import views

urlpatterns = [
    path('logout/', views.logout, name="logout"),
    path('login/', views.login_user, name="login"),
    path('signup/', views.signup, name="signup"),

    path('signupcustomer/', views.signup_customer, name="signup_customer"),
    path('signupseller/', views.signup_seller, name="signup_seller"),
    path('customerPage/', views.customer_page, name="customerPage"),
    path('sellerPage/', views.seller_page, name="sellerPage"),
    path('tos/', views.tos, name="tos"),
    path('tos_user/', views.tos_user, name="tos_user"),
]

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
    path('tos_seller_use/', views.tos_seller_use, name="tos_seller_use"),
    path('tos_seller_private/', views.tos_seller_private, name="tos_seller_private"),
    path('tos_user_use/', views.tos_user_use, name="tos_user_use"),
    path('tos_user_private/', views.tos_user_private, name="tos_user_private"),

]

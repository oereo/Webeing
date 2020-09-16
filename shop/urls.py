from django.urls import path
from .views import *
from django.conf.urls import url

app_name = 'shop'

urlpatterns = [
    path('', restaurant_in_category, name='home'),
    path('<slug:category_slug>/', restaurant_in_category, name='restaurant_in_category'),
    path('<slug:restaurant_slug>/', product_in_restaurant, name='product_in_restaurant'),
    path('<int:id>/<product_slug>/', product_detail, name='product_detail'),
]
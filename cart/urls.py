from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('cart_needs', detail, name='detail'),
    path('add/<int:product_id>', add, name='product_add'),
    path('remove/<product_id>', remove, name='product_remove'),
]

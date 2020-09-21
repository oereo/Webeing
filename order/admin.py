from django.contrib import admin
from .models import Order, OrderItem
from . import models

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created', 'updated']


@admin.register(models.OrderItem)
class OrderItemAdminn(admin.ModelAdmin):
    list_display = ['order', 'product', 'price', 'quantity', 'created', 'updated']

   

#admin.site.register(OrderItem)


from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'business_number', 'food_origin', 'open_time', 'call_number']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Restaurant, RestaurantAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'restaurant', 'price', 'stock', 'available_display', 'available_order', 'created',
                    'updated']
    list_filter = ['available_display', 'created', 'updated', 'restaurant']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'stock', 'available_display', 'available_order']


admin.site.register(Product, ProductAdmin)


class BuyinglistAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock']


admin.site.register(buyingList, BuyinglistAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['owner', 'title', 'pub_date', 'body', 'views']


admin.site.register(Comment, CommentAdmin)

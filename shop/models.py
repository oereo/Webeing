from django.db import models
from Account.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.TextField(blank=True)

    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:restaurant_in_category', args=[self.slug])


class Restaurant(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='restaurants')
    name = models.CharField(max_length=200, db_index=True)

    image = models.ImageField(upload_to='restaurants/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    location = models.TextField(max_length=100, null=True)
    business_number = models.CharField(max_length=30, null=True, unique=False)
    food_origin = models.TextField(max_length=100, null=True)
    open_time = models.CharField(max_length=13, null=True, unique=False)
    call_number = models.CharField(max_length=13, null=True, unique=True)

    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'restaurant'
        verbose_name_plural = 'restauranxts'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_in_restaurant', args=[self.slug])


class Product(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    origin_price = models.IntegerField()
    price = models.IntegerField()  ## [찬규] 가격 정보 정수값으로 수정했습니다.
    discount = models.IntegerField(default=0)
    stock = models.PositiveIntegerField()

    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)

    # 여기서 if 함수를 사용해서 stock=0이면 display order x

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        index_together = [['id', 'slug']]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


class buyingList(models.Model):
    buylist = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='buylists')
    name = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Register(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='Registers')
    name = models.CharField(max_length=200, db_index=True)

    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)

    # 여기서 if 함수를 사용해서 stock=0이면 display order x

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name

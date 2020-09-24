from django.shortcuts import render, get_object_or_404
from .models import Restaurant, Category, Product

def landingPage(request):
    return render(request, 'shop/landingPage.html')


def restaurant_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    restaurants = Restaurant.objects.filter(available_display=True)


    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        restaurants = restaurants.filter(category=current_category)

    return render(request, 'shop/list.html',
                  {'current_category': current_category, 'categories': categories, 'restaurants': restaurants})


from cart.forms import AddProductForm

def product_in_restaurant(request, restaurant_slug=None):
    current_restaurant = None
    restaurants = Restaurant.objects.all()
    products = Product.objects.filter(available_display=True)

    if restaurant_slug:
        current_restaurant = get_object_or_404(Restaurant, slug=restaurant_slug)
        products = products.filter(restaurant=current_restaurant)

    return render(request, 'shop/product_list.html',
                  {'current_restaurant': current_restaurant, 'restaurants': restaurants, 'products': products})


from cart.forms import AddProductForm
def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    add_to_cart = AddProductForm(initial={'quantity':1})
    return render(request, 'shop/detail.html', {'product': product, 'add_to_cart':add_to_cart})



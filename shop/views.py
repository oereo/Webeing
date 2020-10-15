from django.shortcuts import render, get_object_or_404

from cart.cart import Cart
from coupon.forms import AddCouponForm
from .models import Restaurant, Category, Product, Register


def landingPage(request):
    return render(request, 'shop/landingPage.html')


def restaurant_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    restaurants = Restaurant.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        restaurants = restaurants.filter(category=current_category)

    return render(
        request, 'shop/list.html',
        {'current_category': current_category,
         'categories': categories,
         'restaurants': restaurants
         }
    )


def product_in_restaurant(request, restaurant_slug=None):
    current_restaurant = None
    restaurants = Restaurant.objects.all()
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)
    cart = Cart(request)
    add_coupon = AddCouponForm()
    add_to_cart = AddProductForm(initial={'quantity': 1})

    for product in cart:
        product['quantity_form'] = AddProductForm(initial={'quantity': product['quantity'], 'is_update': True})

    if restaurant_slug:
        current_restaurant = get_object_or_404(Restaurant, slug=restaurant_slug)
        products = products.filter(restaurant=current_restaurant).order_by('-id')[:3]

    return render(
        request, 'shop/product_list.html',
        {'current_restaurant': current_restaurant,
         'categories': categories,
         'restaurants': restaurants,
         'products': products,
         'cart': cart,
         'add_coupon': add_coupon,
         'add_to_cart': add_to_cart
         }
    )


from cart.forms import AddProductForm


def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    add_to_cart = AddProductForm(initial={'quantity': 1})
    return render(request, 'shop/detail.html', {'product': product, 'add_to_cart': add_to_cart})


from .forms import RegisterForm
from django.views.generic.edit import FormView


class ProductRegister(FormView):
    template_name = 'product_register.html'
    form_class = RegisterForm
    success_url = '/sellerPage'

    def form_valid(self, form):
        register = Register(
            name=form.data.get('name'),
            price=form.data.get('price'),
            # image = form.data.get('image'),
            stock=form.data.get('stock'),
            description=form.data.get('description')
        )
        temp = register.save()

        return super().form_valid(form)


def add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    add_to_cart = AddProductForm(initial={'quantity': 1})

    form = AddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], is_update=cd['is_update'])

    return render(request, 'shop/product_list.html', {'add_to_cart': add_to_cart})


def remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return render(request, 'shop/product_list.html')

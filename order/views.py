from django.shortcuts import render, get_object_or_404
from .models import *
from cart.cart import Cart
from .forms import *
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie, csrf_protect


def order_create(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    final = 0
    env_point = 0
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save()
            order.user = request.user
            order.save()

            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.amount
                order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                         quantity=item['quantity'])

            cart.clear()
            return render(request, 'order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
        for item in cart:
            final += item['quantity']
            env_point += (item['price'] * item['quantity']) / 10
    return render(request,
                  'order/create.html', {
                      'cart': cart,
                      'form': form,
                      'final': final,
                      'env_point': env_point
                  })


# ajax로 결제 후에 보여줄 결제 완료 화면
@ensure_csrf_cookie
@csrf_protect
def order_complete(request):
    cart = Cart(request)
    user = request.user
    orders = Order.objects.filter(user=user)
    order = Order.objects.filter(user=user).first()
    final = 0
    orderitems_amount = 0

    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                 quantity=item['quantity'])

    cart.clear()

    all_env_point = User.objects.all()

    # 총 환경금액 합산 filtering logic
    total = sum(filter(None, (env_point.env_money for env_point in all_env_point)))

    for order in orders:
        temp = OrderItem.objects.filter(order=order)
        for orderitem in temp:
            user_item = orderitem.order
            final += orderitem.price / 10

    user_success = User.objects.get(user=user_item)
    user_success.env_money = final
    user_success.save()
    return render(request, 'order/created.html', {'orderitems_amount': orderitems_amount, 'total': total})


# 결제를 위한 임포트
from django.views.generic.base import View
from django.http import JsonResponse


class OrderCreateAjaxView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({"authenticated": False}, status=403)

        cart = Cart(request)
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon

                order.discount = cart.coupon.amount
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            data = {
                "order_id": order.id
            }
            return JsonResponse(data)
        else:
            return JsonResponse({}, status=401)


# 결제 정보 생성
class OrderCheckoutAjaxView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({"authenticated": False}, status=403)

        order_id = request.POST.get('order_id')
        order = Order.objects.get(id=order_id)
        amount = request.POST.get('amount')

        try:
            merchant_order_id = OrderTransaction.objects.create_new(
                order=order,
                amount=amount
            )
        except:
            merchant_order_id = None

        if merchant_order_id is not None:
            data = {
                "works": True,
                "merchant_id": merchant_order_id
            }
            return JsonResponse(data)
        else:
            return JsonResponse({}, status=401)


# 실제 결제가 이뤄진 것이 있는지 확인
class OrderImpAjaxView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({"authenticated": False}, status=403)

        order_id = request.POST.get('order_id')
        order = Order.objects.get(id=order_id)
        merchant_id = request.POST.get('merchant_id')
        imp_id = request.POST.get('imp_id')
        amount = request.POST.get('amount')

        try:
            trans = OrderTransaction.objects.get(
                order=order,
                merchant_order_id=merchant_id,
                amount=amount
            )
        except:
            trans = None

        if trans is not None:
            trans.transaction_id = imp_id
            trans.success = True
            trans.save()
            order.paid = True
            order.save()

            data = {
                "works": True
            }

            return JsonResponse(data)
        else:
            return JsonResponse({}, status=401)


def order_payment(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.user = request.user
            order.save()
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.amount
                order.save()
            # for item in cart:
            #     OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
            #                              quantity=item['quantity'])
            #
            # cart.clear()
            return render(request, 'order/payment.html', {'order': order, 'cart': cart})

    else:
        form = OrderCreateForm()
    return render(request, 'order/create.html', {'cart': cart, 'form': form})

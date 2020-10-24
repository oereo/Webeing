from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView

from order.models import OrderItem, Order
from .forms import UserCreationForm
from .models import User


class UserRegistrationView(CreateView):
    model = User  # 자동생성 폼에서 사용할 모델
    fields = ('email', 'phone_number', 'nickname', 'password')  # 자동생성 폼에서 사용할 필드


def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            # return render(request, 'shop/list.html')
            return redirect('/main/')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def signup_customer(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password_confirm']:
            phone_number = request.POST['phonenumber']
            email = request.POST['username']

            if not User.objects.filter(phone_number=phone_number).exists():
                user = User.objects.create_user(
                    # request.POST['email'],
                    phone_number=request.POST['phonenumber'],
                    password=request.POST['password'],
                    email=request.POST['username'],
                    nickname=request.POST['nickname'],
                )
                auth.login(request, user)

                return redirect('/main/')

            elif User.objects.filter(email=email).exists():
                err = 3
                return render(request, 'signupcustomer.html', {'err': err})
            else:
                message = "이미 가입된 계정이 있거나 기입된 내용이 중복됩니다."
                err = 1
                return render(request, 'signupcustomer.html', {'message': message, 'err': err})

        else:
            message = "비밀번호가 일치하지 않습니다."
            err = 2
            return render(request, 'signupcustomer.html', {'message': message, 'err': err})
    else:
        form = UserCreationForm()
    return render(request, 'signupcustomer.html', {'form': form})


def signup_seller(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password_confirm']:
            user = User.objects.create_seller(
                # request.POST['email'],
                phone_number=request.POST['phonenumber'],
                password=request.POST['password'],
                email=request.POST['username'],
                nickname=request.POST['nickname'],
                seller_address=request.POST['seller_address'],
                business_number=request.POST['business_number'],
                seller_name=request.POST['seller_name'],
            )
            auth.login(request, user)

        return redirect('/main/')

    else:
        err = 1
        form = UserCreationForm()
    return render(request, 'signupseller.html', {'form': form, 'err': err})


def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        print('log out success')
        return redirect('/main/')
    return render(request, 'shop/list.html')


def customer_page(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    user_env_point = User.objects.get(email=user.email)
    user_env_point_amount = user_env_point.env_money
    order_items_list = []

    all_env_point = User.objects.all()

    # 총 환경금액 합산 filtering logic
    total = sum(filter(None, (env_point.env_money for env_point in all_env_point)))

    for order in orders:
        order_items_list.append(OrderItem.objects.filter(order=order))

    return render(request, 'customerPage.html', {
        'order_items_list': order_items_list,
        'orders': orders,
        'user_env_point_amount': user_env_point_amount,
        'total': total
    })


def seller_page(request):
    return render(request, 'sellerPage.html')


def signup(request):
    return render(request, 'signup.html')


def tos_seller_use(request):
    return render(request, 'tos_seller_use.html')


def tos_seller_private(request):
    return render(request, 'tos_seller_private.html')


def tos_user_use(request):
    return render(request, 'tos_user_use.html')


def tos_user_private(request):
    return render(request, 'tos_user_private.html')

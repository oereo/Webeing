from django.conf.urls import url
from django.urls import path, include
from Account import views

urlpatterns = [
    path('logout/', views.logout, name ="logout"),
    path('login/', views.login_user, name = "login"),
    path('signup/', views.signup, name = "signup"),
    #path('join/', views.UserRegistrationView.as_view(), name='join'),
]
from django.contrib import admin
from django.urls import path

from .views.payment import Payment
from .views.confirm import Confirm
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.user import UserView
from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('user', auth_middleware(UserView.as_view()), name='user'),
    path('payment', Payment.as_view(), name='payment'),
    path('confirm',Confirm.as_view(), name='confirm')

]

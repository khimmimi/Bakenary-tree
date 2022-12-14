from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect, render
from django.views import View

from store.middlewares.auth import auth_middleware
from store.models.customer import Customer
from store.models.orders import Order
from store.models.product import Products


class UserView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        user=Customer.get_customer(customer)
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        data={
            'orders' : orders,
            'user' : user
        }
        return render(request , 'user.html'  ,data )

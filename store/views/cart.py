from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect, render
from django.views import View

from store.models.product import Products


class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )


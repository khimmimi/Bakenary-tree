from django.shortcuts import render
from django.views import View
from store.models.product import Products

class Payment(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        print(products)
        return render (request, 'payment.html',{'products' : products})

    
    

       

from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect, render
from django.views import View

from store.models.customer import Customer
from store.models.orders import Order
from store.models.payslip import Payslip
from store.models.product import Products
from store.templatetags.cart import price_total
from store.views.payment import Payment


class CheckOut(View):
    def post(self, request):
        sum=0
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)
        customer = request.session.get('customer')
        for product in products:
            sum += price_total(product, cart)
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                        product=product,
                        price=product.price,
                        address=address,
                        phone=phone,
                        quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}
        payslip = Payslip(total_price=sum,
                            customer=Customer(id=customer))
        payslip.getPaySlip()
    
        return redirect('payment')

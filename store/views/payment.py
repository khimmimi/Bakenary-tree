from django.shortcuts import redirect, render
from django.views import View

from store.models.customer import Customer
from store.models.orders import Order
from store.models.payslip import Payslip
from store.models.product import Products


class Payment(View):
    def get(self, request):
        customer = request.session.get('customer')
        payslip=Payslip.get_payslip_by_customer(customer)
        return render(request, 'payment.html', {'payslip':payslip} )

    def post(self, request):
        postData = request.POST
        customer = request.session.get('customer')
        payslip=Payslip.get_payslip_by_customer(customer)
        payslip.payslip_image=request.FILES['payslipImage']
        payslip.getPaySlip()
        return render(request,'confirm.html')
    
    

       

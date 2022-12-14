

from django.db import models

from .customer import Customer
import datetime

class Payslip(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    total_price= models.IntegerField(default=0)
    payslip_image=models.ImageField(upload_to='uploads/payslips/')
    date = models.DateField (default=datetime.datetime.today)

    def getPaySlip(self):
        self.save()

    def get_payslip_by_customer(customer_id):
        return Payslip.objects.filter(customer=customer_id).last()


    
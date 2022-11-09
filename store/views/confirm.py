from django.shortcuts import render
from django.views import View


class Confirm(View):
    def get(self, request):
        return render (request, 'confirm.html')
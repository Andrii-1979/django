from django.shortcuts import render
from . import views

def business(request):
    return render(request, 'business/business.html')

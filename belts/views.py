from django.shortcuts import render
from . import views
from .models import Belt

def belts(request):
    belts = Belt.objects.order_by('data', 'tipe', 'department')
    return render(request, 'belts/belts.html', {'belts':belts})

def belts_department(request):
    belts = Belt.objects.order_by('department', 'data', 'tipe')
    return render(request, 'belts/belts.html', {'belts':belts})

def belts_tipe(request):
    belts = Belt.objects.order_by('tipe', 'data', 'department')
    return render(request, 'belts/belts.html', {'belts':belts})

def belts_data(request):
    belts = Belt.objects.order_by('data', 'department', 'tipe')
    return render(request, 'belts/belts.html', {'belts':belts})

from django.shortcuts import render
from . import views
from .models import Blank

def blanks(request):
    blanks = Blank.objects.order_by('position')
    return render(request, 'blanks/blanks.html', {'blanks':blanks})

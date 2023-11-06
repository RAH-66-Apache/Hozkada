from django.shortcuts import render
from .models import Platerra

# Create your views here.

def index(request): 
    return render(request, 'index.html')

def bokatak(request):
    platerra = Platerra.objects.all
    return render(request, 'bokatak.html', {'bokatak':platerra})
from django.shortcuts import render
from .models import Platerra
from .models import Alergia_Platerra, Bezeroa


# Create your views here.

def index(request): 
    return render(request, 'index.html')

def bokatak(request):
    platerra = Platerra.objects.all
    alergia_platerrak = Alergia_Platerra.objects.all
    return render(request, 'bokatak.html', {'bokatak':platerra,'alergia_platerrak':alergia_platerrak})

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')


from django.shortcuts import render
from .models import Platerra
from .models import Alergia_Platerra
from .models import Bezeroa 
# Create your views here.

def index(request): 
    return render(request, 'index.html')

def perfil(request): 
    return render(request, 'perfil.html')

def bokatak(request):
    platerra = Platerra.objects.all
    alergia_platerrak = Alergia_Platerra.objects.all
    return render(request, 'bokatak.html', {'bokatak':platerra,'alergia_platerrak':alergia_platerrak})

def imagenperfil(request):
    # Obtiene el objeto Bezeroa relacionado con el usuario autenticado
    bezeroa = Bezeroa.objects.get(user=request.user)

    # Pasa el objeto Bezeroa a la plantilla
    return render(request, 'index.html', {'bezeroa': bezeroa})
from django.shortcuts import render
from .models import Platerra
from .models import Alergia_Platerra
from .models import Bezeroa 
from django.http import HttpResponseRedirect
from django.urls import reverse
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

def updatebezeroa(request,id):
    
    izena = request.POST['izena']
    abizena = request.POST['abizena']
    abizena2 = request.POST['abizena2']
    nan = request.POST['nan']
    telefonoa = request.POST['telefonoa']
    emaila = request.POST['emaila']
    helbidea = request.POST['helbidea']
    postalkodea = request.POST['pk']

    bezeroa = Bezeroa.objects.get(id = id)
    bezeroauser = bezeroa.user
    bezeroauser.id = bezeroa.user_id
    bezeroauser.save()
    bezeroa.izena = izena
    bezeroa.abizena = abizena
    bezeroa.abizena2 = abizena2
    bezeroa.NAN = nan
    bezeroa.telefonoa = telefonoa
    bezeroa.emaila = emaila
    bezeroa.helbidea = helbidea
    bezeroa.pk = postalkodea
    

    bezeroa.save()
    return HttpResponseRedirect(reverse('index'))

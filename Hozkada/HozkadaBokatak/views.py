from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Platerra
from.models import User
from .models import Bezeroa
from .models import Alergia_Platerra

# Create your views here.

def index(request): 
    return render(request, 'index.html')

def bokatak(request):
    platerra = Platerra.objects.all
    alergia_platerrak = Alergia_Platerra.objects.all
    return render(request, 'bokatak.html', {'bokatak':platerra,'alergia_platerrak':alergia_platerrak})

def register_bezeroa(request):
    return render(request, 'register_user.html')

def register_bezeroa_erregistroa(request):
    if request.method == 'POST':
        nan = request.POST['nan']
        izena = request.POST['izena']
        abizena = request.POST['abizena']
        abizena2 = request.POST['abizena2']
        telefonoa = request.POST['telefonoa']
        emaila = request.POST['email']
        pasahitza = request.POST['pasahitza']
        helbidea = request.POST['helbidea']
        postakodea = request.POST['pk']
        argazkia = request.FILES['argazkia']

        # Create a User instance
        user = User.objects.create_user(username=izena, password=pasahitza)
        
        # Create a Bezeroa instance linked to the user
        bezeroa = Bezeroa(
            user=user,  # Link the Bezeroa model to the user
            nan=nan,
            izena=izena,
            abizena=abizena,
            abizena2=abizena2,
            telefonoa=telefonoa,
            emaila=emaila,
            helbidea=helbidea,
            postakodea=postakodea,
            img = argazkia
        )

        bezeroa.save()
        return HttpResponseRedirect(reverse('index'))
    
def perfil(request):
    return render(request, 'perfil.html')
    
def update_bezeroa(request):
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
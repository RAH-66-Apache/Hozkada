from django.shortcuts import render,redirect
from .models import Platerra
from .models import Alergia_Platerra, Eskaera, Platerra_Eskaera
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request): 
    return render(request, 'index.html')

def bokatak(request):
    platerra = Platerra.objects.all
    alergia_platerrak = Alergia_Platerra.objects.all
    return render(request, 'bokatak.html', {'bokatak':platerra,'alergia_platerrak':alergia_platerrak})


#  Con esta funcion estoy tratando de crear una nueva escaera y al mismo tiempo crear un nuevo platerra_eskaera
@login_required
def agregar_bocata_al_carrito(request,platerra_id): 

    # Obtén el usuario actual y verifica si ya tiene una Eskaera activa
    user = request.user
    eskaera = Eskaera.objects.filter(id_bezeroa=user.bezeroa, egoera=False).first()

    # Si no existe una Eskaera activa, crea una nueva
    if not eskaera:
        eskaera = Eskaera(id_bezeroa=user.bezeroa, egoera=False)
        eskaera.save()
    # Obten el platerra seleccionado por su id
    platerra = Platerra.objects.get(id=platerra_id)

    # Ahora, crea o actualiza la relación Platerra_Eskaera
    platerra_eskaera, created = Platerra_Eskaera.objects.get_or_create(eskaera_id=eskaera, platerra_id=platerra)

    #Aumenta la cantidad en 1
    platerra_eskaera.kantitatea += 1
    platerra_eskaera.save()

    # Devuelve una respuesta JSON
    response_data = {"success": True,"platerra_nombre": platerra.izena}  # Cambia a False si hay un error
    return JsonResponse(response_data)

def lista_carrito(request):
    # Obtén los elementos del carrito
    elementos_carrito = Platerra_Eskaera.objects.filter(
        eskaera_id__id_bezeroa=request.user.bezeroa,
        eskaera_id__egoera=False
    )

    # Prepara los datos a mostrar en el div
    carrito_data = [f"{elemento.platerra_id.izena}" for elemento in elementos_carrito]

    # Crea una respuesta JSON con los datos del carrito
    response_data = {
        'carrito_data': carrito_data,
    }

    return JsonResponse(response_data)
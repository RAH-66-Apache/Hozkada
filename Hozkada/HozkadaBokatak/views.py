from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,reverse
from .models import Platerra
from .models import Alergia_Platerra, Eskaera, Platerra_Eskaera
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
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
        username = request.POST['username']
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
        user = User.objects.create_user(username=username, password=pasahitza)
        
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
    
def update_bezeroa(request, id):
    if request.method == 'POST':
        izena = request.POST['izena']
        abizena = request.POST['abizena']
        abizena2 = request.POST['abizena2']
        nan = request.POST['nan']
        telefonoa = request.POST['telefonoa']
        emaila = request.POST['email']
        helbidea = request.POST['helbidea']
        postalkodea = request.POST['pk']
        username = request.POST['username']

        bezeroa = Bezeroa.objects.get(user_id=id)

        bezeroa.izena = izena
        bezeroa.abizena = abizena
        bezeroa.abizena2 = abizena2
        bezeroa.nan = nan
        bezeroa.telefonoa = telefonoa
        bezeroa.emaila = emaila
        bezeroa.helbidea = helbidea
        bezeroa.postakodea = postalkodea
        bezeroa.save()
        # Guardar los cambios en la base de datos

        user = User.objects.get(id=id)
        user.username = username
        user.save()

        # Redireccionar a la página 'index'
        return HttpResponseRedirect(reverse('index'))

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

     # Guarda la información del carrito en la sesión del usuario
    request.session['carrito'] = list(Platerra_Eskaera.objects.filter(eskaera_id=eskaera).values('platerra_id__izena', 'kantitatea'))
    # Devuelve una respuesta JSON
    response_data = {"success": True,"platerra_nombre": platerra.izena}  # Cambia a False si hay un error
    return JsonResponse(response_data)
@login_required
def lista_carrito(request):
    # Obtén los elementos del carrito
    elementos_carrito = Platerra_Eskaera.objects.filter(
        eskaera_id__id_bezeroa=request.user.bezeroa,
        eskaera_id__egoera=False
    )

    # Prepara los datos a mostrar en el div
    carrito_data = [{"izena": elemento.platerra_id.izena, "kantitatea": elemento.kantitatea,"prezioa": elemento.platerra_id.prezioa} for elemento in elementos_carrito]

    # Crea una respuesta JSON con los datos del carrito
    response_data = {
        'carrito_data': carrito_data,
    }

    return JsonResponse(response_data)


@login_required
def actualizar_cantidad(request):
    if request.method == 'POST':
        platerra_nombre = request.POST.get('platerra_nombre')
        nueva_cantidad = request.POST.get('nueva_cantidad')

        # Obtiene el precio unitario del Platerra
        platerra = Platerra.objects.get(izena=platerra_nombre)
        precio_unitario = platerra.prezioa

        # Actualiza la cantidad en la base de datos según el nombre del platerra
        Platerra_Eskaera.objects.filter(
            eskaera_id__id_bezeroa=request.user.bezeroa,
            eskaera_id__egoera=False,
            platerra_id__izena=platerra_nombre
        ).update(kantitatea=nueva_cantidad)

        response_data = {
            "success": True,
            "precio_unitario": precio_unitario
        }
        return JsonResponse(response_data)
    else:
        response_data = {"success": False, "redirect": reverse('login')}
        return JsonResponse(response_data)
    

@login_required
def eliminar_del_carrito(request):
    print("Entrando en eliminar_del_carrito")
    platerra_eskaera_id = request.POST.get('platerra_eskaera_id', None)
    print("Platerra Eskaera ID:", platerra_eskaera_id)

    if platerra_eskaera_id is not None and platerra_eskaera_id != 'undefined':
        # Utiliza directamente get_object_or_404 sin especificar id=id
        platerra_eskaera = get_object_or_404(Platerra_Eskaera, id=platerra_eskaera_id)

        # Elimina el platerra_eskaera
        platerra_eskaera.delete()

        # Devuelve una respuesta JSON
        response_data = {"success": True}  # Cambia a False si hay un error
    else:
        response_data = {"success": False, "error": "platerra_eskaera_id no proporcionado en la solicitud"}

    return JsonResponse(response_data)

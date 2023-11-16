from datetime import datetime, timezone
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
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

from HozkadaBokatak.models import Bezeroa



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
        bidalketaKostua = request.POST['bidalketaKostua']

        # Create a User instance
        user = User.objects.create_user(username=username, email=emaila, password=pasahitza)
        
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
            img = argazkia,
            bidalketaKostua = bidalketaKostua
        )

        bezeroa.save()
        return HttpResponseRedirect(reverse('index'))
    
def perfil(request):
    return render(request, 'perfil.html')

@login_required
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
        bidalketaKostua = request.POST['bidalketaKostua']
        bezeroa = Bezeroa.objects.get(user_id=id)

        if 'argazkia' in request.FILES:
            argazkia = request.FILES['argazkia']
            bezeroa.img = argazkia


        bezeroa.izena = izena
        bezeroa.abizena = abizena
        bezeroa.abizena2 = abizena2
        bezeroa.nan = nan
        bezeroa.telefonoa = telefonoa
        bezeroa.emaila = emaila
        bezeroa.helbidea = helbidea
        bezeroa.postakodea = postalkodea
        bezeroa.bidalketaKostua = bidalketaKostua
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
def marcar_eskaera_completada(request):
    try:
        user = request.user
        eskaera = Eskaera.objects.filter(id_bezeroa=user.bezeroa, egoera=False).first()

        if eskaera:
            eskaera.egoera = True
            eskaera.save()

            response_data = {"success": True}
        else:
            response_data = {"success": False, "error": "No hay Eskaera activa"}

        return JsonResponse(response_data)
    except Exception as e:
        print(e)
        response_data = {"success": False, "error": str(e)}
        return JsonResponse(response_data)



@login_required
def lista_carrito(request):
    # Obtén los elementos del carrito
    elementos_carrito = Platerra_Eskaera.objects.filter(
        eskaera_id__id_bezeroa=request.user.bezeroa,
        eskaera_id__egoera=False
    )

    # Prepara los datos a mostrar en el div
    carrito_data = [{"id": elemento.id,"izena": elemento.platerra_id.izena, "kantitatea": elemento.kantitatea,"prezioa":elemento.platerra_id.precio_con_descuento()} for elemento in elementos_carrito]

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
        precio_unitario = platerra.precio_con_descuento()

        print("Precio Unitario:", precio_unitario)


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
    platerra_eskaera_id = request.POST.get('platerra_eskaera_id', None)
    print("Entrando en eliminar_del_carrito")
    
    print("Platerra Eskaera ID:", platerra_eskaera_id)

    if platerra_eskaera_id is not None and platerra_eskaera_id != 'undefined':
        # Utiliza directamente get_object_or_404 sin especificar id=id
        platerra_eskaera = Platerra_Eskaera.objects.get(id=platerra_eskaera_id)


        # Elimina el platerra_eskaera
        platerra_eskaera.delete()

        # Devuelve una respuesta JSON
        response_data = {"success": True}  # Cambia a False si hay un error
    else:
        response_data = {"success": False, "error": "platerra_eskaera_id no proporcionado en la solicitud"}

    return JsonResponse(response_data)



@login_required
def eskaera(request):
    print("ENTRANDO EN ESKAERA")
    eskaeras = Eskaera.objects.filter(id_bezeroa=request.user.bezeroa).order_by('-data')

    # Calcula el total para cada Eskaera
    for eskaera in eskaeras:
        eskaera.total = sum(
            platerra_eskaera.kantitatea * platerra_eskaera.platerra_id.precio_con_descuento()
            for platerra_eskaera in Platerra_Eskaera.objects.filter(eskaera_id=eskaera)
        )
        eskaera.time_difference = calculate_time_difference(eskaera.data)

    return render(request, 'eskaera.html', {'eskaeras': eskaeras})



def calculate_time_difference(date):
    # Asegúrate de que date sea un objeto datetime con información de zona horaria
    if date.tzinfo is None:
        date = date.replace(tzinfo=timezone.utc)

    now = datetime.now(timezone.utc)
    difference = now - date
    days = difference.days
    hours, remainder = divmod(difference.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    if days > 0:
        if hours > 0:
            return f"{days} {'Egun' if days == 1 else 'Egun'} {hours} {'Ordu' if hours == 1 else 'Ordu'}"
        else:
            return f"{days} {'Egun' if days == 1 else 'Egun'}"
    elif hours > 0:
        return f"{hours} {'Ordu' if hours == 1 else 'Ordu'}"
    elif minutes > 0:
        return f"{minutes} {'minutu' if minutes == 1 else 'minutu'}"
    else:
        return "Oraintxe bertan"


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("Errore bat egon da erabiltzailea sartzerakoan, saiatu berriro..."))
            return redirect('login')

    
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    return redirect('index')


# AJUSTES
#---------------------------------------
from .forms import BezeroaForm, PlaterraForm

from django.shortcuts import render, redirect
from .forms import BezeroaForm, PlaterraForm
from .models import Bezeroa, Platerra

def ezarpenak(request):
    print("hola")
    bezeroa_form = BezeroaForm()
    platerra_form = PlaterraForm()

    context = {
        'bezeroak': Bezeroa.objects.all(),
        'platerrak': Platerra.objects.all(),
        'bezeroa_form': bezeroa_form,
        'platerra_form': platerra_form,
    }

    return render(request, 'ezarpenak.html', context)

def lista_bezeroak(request):
    bezeroak = Bezeroa.objects.all()
    return render(request, 'lista_bezeroak.html', {'bezeroak': bezeroak})

def crear_bezeroa(request):
    if request.method == 'POST':
        form = BezeroaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ezarpenak')  # Cambiado a 'ezarpenak'
    else:
        form = BezeroaForm()
    return render(request, 'crear_bezeroa.html', {'form': form})

def editar_bezeroa(request, id):
    print("a entrado")
    bezeroa = Bezeroa.objects.get(id=id)

    if request.method == 'POST':
        form = BezeroaForm(request.POST, instance=bezeroa)
        if form.is_valid():
            form.save()
            # Redirigir a la página de inicio después de guardar los cambios
            return redirect('ezarpenak')  # Reemplaza 'nombre_de_tu_index_html' con el nombre correcto de tu URL
    else:
        # Rellenar el formulario con los valores actuales del objeto Bezeroa
        form = BezeroaForm(instance=bezeroa)

    context = {
        'bezeroak': Bezeroa.objects.all(),
        'bezeroa_form': form.as_table(),
    }

    return render(request, 'ezarpenak.html', context)


def obtener_datos_bezeroa(request, id):
    # Obtener el objeto Bezeroa
    bezeroa = get_object_or_404(Bezeroa, id=id)

    # Rellenar el formulario con los valores actuales del objeto Bezeroa
    form = BezeroaForm(instance=bezeroa)

    # Obtener los campos del formulario como HTML
    form_fields_html = form.as_table()

    # Devolver la respuesta como JSON
    return JsonResponse({'form_fields_html': form_fields_html})

def eliminar_bezeroa(request, id):
    bezeroa = Bezeroa.objects.get(id=id)
    bezeroa.delete()
    return redirect('ezarpenak')  # Cambiado a 'ezarpenak'

def lista_platerrak(request):
    platerrak = Platerra.objects.all()
    return render(request, 'lista_platerrak.html', {'platerrak': platerrak})

def crear_platerra(request):
    if request.method == 'POST':
        form = PlaterraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ezarpenak')  # Cambiado a 'ezarpenak'
    else:
        form = PlaterraForm()
    return render(request, 'crear_platerra.html', {'form': form})

def editar_platerra(request, id):
    platerra = Platerra.objects.get(id=id)
    if request.method == 'POST':
        form = PlaterraForm(request.POST, instance=platerra)
        if form.is_valid():
            form.save()
            return redirect('ezarpenak')  # Cambiado a 'ezarpenak'
    else:
        form = PlaterraForm(instance=platerra)
    return render(request, 'editar_platerra.html', {'form': form, 'platerra': platerra})

def eliminar_platerra(request, id):
    platerra = Platerra.objects.get(id=id)
    platerra.delete()
    return redirect('ezarpenak')  # Cambiado a 'ezarpenak'

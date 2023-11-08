from django.shortcuts import render,redirect
from .models import Platerra
from .models import Alergia_Platerra, Eskaera, Platerra_Eskaera
from django.http import JsonResponse
# Create your views here.

def index(request): 
    return render(request, 'index.html')

def bokatak(request):
    platerra = Platerra.objects.all
    alergia_platerrak = Alergia_Platerra.objects.all
    return render(request, 'bokatak.html', {'bokatak':platerra,'alergia_platerrak':alergia_platerrak})

def bokatak_erakutsi(request): #carrito_de_compras
    if request.user.is_authenticated:
        eskaera = Eskaera.objects.get(id_bezeroa=request.user.bezeroa, egoera=True)
        productos_en_carrito = Platerra_Eskaera.objects.filter(eskaera_id=eskaera)
        total = sum(producto.kantitatea * producto.platerra_id.prezioa for producto in productos_en_carrito)
        return render(request, 'carrito.html', {'productos_en_carrito': productos_en_carrito, 'total': total})
    else:
        # Manejar el caso en el que el usuario no esté autenticado
        return redirect('login')  # Redirigir al inicio de sesión o al registro
    
def bokatak_eskaera_gehitu(request): #agregar_al_carrito
    if request.user.is_authenticated:
        eskaera = Eskaera.objects.get(id_bezeroa=request.user.bezeroa, egoera=True)
        platerra_id = request.POST.get('platerra_id')
        kantitatea = int(request.POST.get('kantitatea'))
        
        # Verificar si el producto ya está en el carrito
        producto_en_carrito, created = Platerra_Eskaera.objects.get_or_create(eskaera_id=eskaera, platerra_id=platerra_id)
        
        # Actualizar la cantidad
        if not created:
            producto_en_carrito.kantitatea += kantitatea
            producto_en_carrito.save()
        
        return JsonResponse({'success': True})
    else:
        # Manejar el caso en el que el usuario no esté autenticado
        return JsonResponse({'success': False, 'message': 'Usuario no autenticado'})


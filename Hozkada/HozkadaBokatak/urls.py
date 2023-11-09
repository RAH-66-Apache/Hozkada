from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'), 

    path('bokatak/', views.bokatak, name = 'bokatak'),

   path('bokatak/agregar_bocata_al_carrito/<int:platerra_id>/', views.agregar_bocata_al_carrito, name='agregar_bocata_al_carrito'),

   path('bokatak/lista_carrito/', views.lista_carrito, name='lista_carrito'),

]
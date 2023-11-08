from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'), 

    path('bokatak/', views.bokatak, name = 'bokatak'),

     path('bokatakErakutsi/', views.bokatak_erakutsi, name='bokatak_erakutsi'),

    # Ruta para agregar un producto al carrito
    path('bokatak_eskaera_gehitu/', views.bokatak_eskaera_gehitu, name='bokatak_eskaera_gehitu'),

]
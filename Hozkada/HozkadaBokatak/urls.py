from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'), 

    path('perfil/', views.perfil, name = 'perfil'),

    path('bokatak/', views.bokatak, name = 'bokatak'),

]
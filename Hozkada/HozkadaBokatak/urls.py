from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'), 

    path('bokatak/', views.bokatak, name = 'bokatak'),

    path('gehitubezeroa/', views.register_bezeroa, name='register_user'),
    path('gehitubezeroa/gehitubezeroaerregistroa/', views.register_bezeroa_erregistroa, name='registerbezeroaerregistroa'),

    path('perfil/', views.perfil, name='perfil'),
    path('perfil/updatebezeroa/<id>', views.update_bezeroa, name="updatebezeroa")
]
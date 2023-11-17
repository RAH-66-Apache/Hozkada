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
    path('perfil/updatebezeroa/<id>', views.update_bezeroa, name="updatebezeroa"),

    path('bokatak/agregar_bocata_al_carrito/<int:platerra_id>/', views.agregar_bocata_al_carrito, name='agregar_bocata_al_carrito'),

    path('bokatak/lista_carrito/', views.lista_carrito, name='lista_carrito'),

    path('bokatak/actualizar_cantidad/', views.actualizar_cantidad, name='actualizar_cantidad'),

    path('bokatak/eliminar_del_carrito/', views.eliminar_del_carrito, name='eliminar_del_carrito'),

    path('bokatak/marcar_eskaera_completada/', views.marcar_eskaera_completada, name='marcar_eskaera_completada'),

    

    path('eskaera/', views.eskaera, name='eskaera'),

    path('login_user', views.login_user, name='login'),
    path('logout_user', views. logout_user, name='logout'),

    #AJUSTES
    path('ezarpenak/', views.ezarpenak, name='ezarpenak'),
    path('lista_bezeroak/', views.lista_bezeroak, name='lista_bezeroak'),
    path('crear_bezeroa/', views.crear_bezeroa, name='crear_bezeroa'),
    path('editar_bezeroa/<int:id>/', views.editar_bezeroa, name='editar_bezeroa'),
    path('eliminar_bezeroa/<int:id>/', views.eliminar_bezeroa, name='eliminar_bezeroa'),
    path('obtener_datos_bezeroa/<int:id>/', views.obtener_datos_bezeroa, name='obtener_datos_bezeroa'),




    path('lista_platerrak/', views.lista_platerrak, name='lista_platerrak'),
    path('crear_platerra/', views.crear_platerra, name='crear_platerra'),
    path('editar_platerra/<int:id>/', views.editar_platerra, name='editar_platerra'),
    path('eliminar_platerra/<int:id>/', views.eliminar_platerra, name='eliminar_platerra'),
    path('obtener_datos_platerra/<int:id>/', views.obtener_datos_platerra, name='obtener_datos_platerra'),
]
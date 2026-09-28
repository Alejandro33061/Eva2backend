from django.urls import path
from . import views

urlpatterns = [
    # Rutas de los catálogos
    path('', views.inicio_tienda, name='inicio_tienda'),
    path('juegos/', views.catalogo_juegos, name='catalogo_juegos'),
    path('consolas/', views.catalogo_consolas, name='catalogo_consolas'),
    path('accesorios/', views.catalogo_accesorios, name='catalogo_accesorios'),
    
    # Rutas del sistema de usuarios
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('logout/', views.logout_usuario, name='logout_usuario'),
    path('recuperar/', views.recuperar_password, name='recuperar_password'),
]
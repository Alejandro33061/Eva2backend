from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_accesorios, name='inicio_accesorios'),
    path('catalogo/', views.catalogo_accesorios, name='catalogo_accesorios'),
]
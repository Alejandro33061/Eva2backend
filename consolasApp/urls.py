from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_consolas, name='inicio_consolas'),
    path('catalogo/', views.catalogo_consolas, name='catalogo_consolas'),
]
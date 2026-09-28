from django.shortcuts import render
from .models import Accesorio

def inicio_accesorios(request):
    return render(request, 'accesorios/inicio.html')

def catalogo_accesorios(request):
    accesorios = Accesorio.objects.all()
    return render(request, 'accesorios/catalogo.html', {'accesorios': accesorios})
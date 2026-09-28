from django.shortcuts import render
from .models import Consola

def inicio_consolas(request):
    return render(request, 'consolas/inicio.html')

def catalogo_consolas(request):
    consolas = Consola.objects.all()
    return render(request, 'consolas/catalogo.html', {'consolas': consolas})
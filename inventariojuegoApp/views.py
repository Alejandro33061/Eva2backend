from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# --- 1. IMPORTACIONES DE LA BASE DE DATOS (ORM) ---
from .models import Juego, Plataforma
from consolasApp.models import Consola
from accesoriosApp.models import Accesorio

# --- 2. VISTAS DE LOS CATÁLOGOS ---
def inicio_tienda(request):
    return render(request, 'inventario/inicio.html')

def catalogo_juegos(request):
    # Consulta a la base de datos real
    juegos = Juego.objects.all()
    return render(request, 'inventario/catalogo.html', {'juegos': juegos})

def catalogo_consolas(request):
    # Consulta a la base de datos real
    consolas = Consola.objects.all()
    return render(request, 'consolas/catalogo.html', {'consolas': consolas})

def catalogo_accesorios(request):
    # Consulta a la base de datos real
    accesorios = Accesorio.objects.all()
    return render(request, 'accesorios/catalogo.html', {'accesorios': accesorios})


# --- 3. SISTEMA DE USUARIOS ---
def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_usuario')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio_tienda')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_usuario(request):
    logout(request)
    return redirect('inicio_tienda')

def recuperar_password(request):
    return render(request, 'usuarios/recuperar.html')
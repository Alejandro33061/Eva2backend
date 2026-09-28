from django.contrib import admin
from .models import Plataforma, Juego

admin.site.register(Plataforma)
# Esta configuración permite al profesor buscar registros directamente en el panel
@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'plataforma', 'precio')
    search_fields = ('titulo', 'genero')
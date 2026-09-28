from django.contrib import admin
from .models import Accesorio

@admin.register(Accesorio)
class AccesorioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'marca', 'tipo', 'precio')
    search_fields = ('producto', 'tipo')
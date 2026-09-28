from django.db import models
from consolasApp.models import Marca 

class Accesorio(models.Model):
    producto = models.CharField(max_length=100, verbose_name="Nombre del Accesorio")
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name="accesorios")
    tipo = models.CharField(max_length=50, verbose_name="Tipo (Ej: Audio, Mando)")
    precio = models.IntegerField(verbose_name="Precio")
    imagen = models.CharField(max_length=255, verbose_name="Ruta de Imagen")

    def __str__(self):
        return self.producto

    class Meta:
        verbose_name = "Accesorio"
        verbose_name_plural = "Accesorios"
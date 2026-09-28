from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Nombre de Marca")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

class Consola(models.Model):
    equipo = models.CharField(max_length=100, verbose_name="Nombre del Equipo")
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name="consolas")
    almacenamiento = models.CharField(max_length=50, verbose_name="Almacenamiento")
    precio = models.IntegerField(verbose_name="Precio")
    imagen = models.CharField(max_length=255, verbose_name="Ruta de Imagen")

    def __str__(self):
        return f"{self.marca.nombre} {self.equipo}"

    class Meta:
        verbose_name = "Consola"
        verbose_name_plural = "Consolas"
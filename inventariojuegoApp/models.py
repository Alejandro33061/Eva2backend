from django.db import models

class Plataforma(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Nombre de Plataforma")

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Plataforma"
        verbose_name_plural = "Plataformas"

class Juego(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título del Juego")
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE, related_name="juegos")
    genero = models.CharField(max_length=50, verbose_name="Género")
    precio = models.IntegerField(verbose_name="Precio")
    imagen = models.CharField(max_length=255, verbose_name="Ruta de Imagen (Ej: img/juego.jpg)")

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"
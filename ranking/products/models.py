from django.db import models

# Create your models here.

class Game(models.Model):
    id = models.IntegerField(verbose_name='Id', primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Nombre')
    platform = models.CharField(max_length=4, verbose_name='Plataforma')
    score = models.IntegerField(verbose_name='Puntaje')
    image = models.CharField(max_length=300, verbose_name='Imagen')

    class Meta:
        verbose_name = 'Juego'
        verbose_name_plural = 'Juegos'
        ordering = ['score']

    def __str__(self):
        return self.name

class Platform(models.Model):
    name = models.CharField(max_length=4, verbose_name='Nombre', primary_key=True)

    class Meta:
        verbose_name = 'Plataforma'
        verbose_name_plural = 'Plataformas'
        ordering = ['name']

    def __str__(self):
        return self.name

class Image(models.Model):
    route = models.CharField(max_length=300, verbose_name='Ruta')
    game = models.IntegerField(verbose_name='Game Id', primary_key=True)

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'
        ordering = ['game']


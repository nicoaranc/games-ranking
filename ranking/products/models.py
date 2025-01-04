from django.db import models

# Create your models here.

class Game(models.Model):
    id = models.IntegerField(verbose_name='Id', primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Nombre')
    platform = models.CharField(max_length=4, verbose_name='Plataforma')
    score = models.IntegerField(verbose_name='Puntaje')
    image = models.CharField(max_length=300, verbose_name='Imagen')

class Platform(models.Model):
    name = models.CharField(max_length=4, verbose_name='Nombre', primary_key=True)

class Image(models.Model):
    route = models.CharField(max_length=300, verbose_name='Ruta')
    game = models.IntegerField(verbose_name='Game Id', primary_key=True)


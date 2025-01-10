from django.db import models
from PIL import Image as IMG
from io import BytesIO
from django.core.files import File

# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=4, verbose_name='Nombre', primary_key=True)
    slug = models.SlugField

    class Meta:
        verbose_name = 'Plataforma'
        verbose_name_plural = 'Plataformas'
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'


class Game(models.Model):
    # id = models.IntegerField(verbose_name='Id', primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Nombre')
    platform = models.ForeignKey(Platform, related_name='games', on_delete=models.CASCADE, verbose_name='Plataforma')
    score = models.IntegerField(verbose_name='Puntaje')
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        verbose_name = 'Juego'
        verbose_name_plural = 'Juegos'
        ordering = ['-score']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.platform.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
            else:
                return ''

    def make_thumbnail(self, image, size=(256,256)):
        img = IMG.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


class Image(models.Model):
    route = models.CharField(max_length=300, verbose_name='Ruta')
    game = models.IntegerField(verbose_name='Game Id', primary_key=True)

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'
        ordering = ['game']


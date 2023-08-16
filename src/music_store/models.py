from datetime import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "artists"

class Album(models.Model):
    artist = models.ForeignKey(
        "Artist", related_name="albums", on_delete=models.CASCADE
    )
    year_created = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)]
     )

    def __str__(self):
        return self.year_created

    class Meta:
        ordering = ["year_created"]
        verbose_name_plural = "albums"

class Song(models.Model):
    title = models.CharField(max_length=100)
    albums = models.ManyToManyField('Album', through='SongsAndAlbums')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "songs"


class SongsAndAlbums(models.Model):
    '''
    Модель для связи «многие ко многим»:
    - связь «один ко многим» с моделью Song;
    - связь «один ко многим» с моделью Album.
    - порядковый номер песни на альбоме
    '''
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    song = models.ForeignKey('Song', on_delete=models.CASCADE)
    song_number = models.IntegerField(validators=[MinValueValidator(1)])

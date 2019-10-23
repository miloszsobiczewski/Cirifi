from django.db import models

from music.models import Playlist


class Que(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)


class Config(models.Model):
    device = models.CharField(max_length=25)
    storage_path = models.FilePathField()

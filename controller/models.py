from django.db import models

from music.models import Playlist

STATUSES = [
    ("Ready", "ready"),
    ("Playing", "playing"),
    ("Paused", "paused"),
    ("Stopped", "stopped"),
]


class Que(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    status = models.CharField(
        choices=STATUSES, blank=True, default="ready", max_length=16
    )
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.date.strftime('%Y-%m-%d %H:%M')}] {self.name}"


class Config(models.Model):
    device = models.CharField(max_length=25)
    storage_path = models.FilePathField()

    def __str__(self):
        return self.device

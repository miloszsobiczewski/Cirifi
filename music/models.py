from django.db import models


class Playlist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=100)
    playlist = models.ForeignKey(
        Playlist, related_name='albums', null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.location


class Song(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
    playlist = models.ForeignKey(
        Playlist, related_name='songs', null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"[{self.album}] {self.name}"




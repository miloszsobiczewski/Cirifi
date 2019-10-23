from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.location


class Song(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"[{self.album}] {self.name}"


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    # todo: change to many to many field
    songs = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

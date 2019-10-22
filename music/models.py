from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=100)
    location = models.FilePathField()


class Song(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL)


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ForeignKey(Song)

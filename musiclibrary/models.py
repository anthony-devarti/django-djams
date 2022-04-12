from django.db import models

# Create your models here.
from django.db import models


class Album(models.Model):
    album_name = models.CharField(max_length=50)
    def __str__(self):
        return self.album_name

class Song(models.Model):
    song_title = models.CharField(max_length=50)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    def __str__(self):
        return self.song_title

class Playlist(models.Model):
    playlist_title = models.CharField(max_length=50)
    def __str__(self):
        return self.playlist_title

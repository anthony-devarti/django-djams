from django.shortcuts import render
from .models import Song, Album, Playlist


# Create your views here.
from django.http import HttpResponse, JsonResponse

def index(request):
    #grab all of the songs
    recent_songs = Song.objects.all()
    #get the values from them
    recent2 = recent_songs.values()
    #turn them into a list
    recent3 = list(recent2)
    #return them with keys
    return JsonResponse({ 'data' : recent3 })

def song_find(request, song_id):
    response = "This is song number %s."
    return HttpResponse(response % song_id)
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from src.music_store.models import Artist, Album, Song, SongsAndAlbums
from src.music_store.serializers import ArtistSerializer, AlbumSerializer, SongsSerializer, SongsAndAlbumSerializer


# Create your views here.

class ArtistCreate(generics.CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistList(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumCreate(generics.CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumList(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongCreate(generics.CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongsSerializer

class SongList(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongsSerializer


class AddSongToAlbum(generics.CreateAPIView):
    queryset = SongsAndAlbums.objects.all()
    serializer_class = SongsAndAlbumSerializer
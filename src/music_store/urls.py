from django.urls import path

from src.music_store import views

urlpatterns = [
    # ARTIST MANAGEMENT API
    path("artists/create", views.ArtistCreate.as_view(), name="create_artist"),
    path("artists/list", views.ArtistList.as_view(), name="artist_list"),
    # ALBUMS MANAGEMENT API
    path("albums/create", views.AlbumCreate.as_view(), name="create_album"),
    path("albums/list", views.AlbumList.as_view(), name="album_list"),
    # SONGS MANAGEMENT API
    path("songs/create", views.SongCreate.as_view(), name="create_song"),
    path("songs/list", views.SongList.as_view(), name="song_list"),
    path("songs/add_song_to_album", views.AddSongToAlbum.as_view(), name="add_song_to_album"),
]

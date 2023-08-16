from django.urls import path

from src.music_store import views

urlpatterns = [
    # ARTIST MANAGEMENT API
    path("artists/create", views.ArtistCreate.as_view(), name="create_artist"),
    path("artists/list", views.ArtistList.as_view(), name="artist_list"),
    path("artists/detail/<int:pk>", views.ArtistDetail.as_view(), name="artist_detail"),
    path("artists/update/<int:pk>", views.ArtistUpdate.as_view(), name="artist_update"),
    path("artists/delete/<int:pk>", views.ArtistDelete.as_view(), name="artist_delete"),
    # ALBUMS MANAGEMENT API
    path("albums/create", views.AlbumCreate.as_view(), name="create_album"),
    path("albums/list", views.AlbumList.as_view(), name="album_list"),
    path("albums/detail/<int:pk>", views.AlbumDetail.as_view(), name="album_detail"),
    path("albums/update/<int:pk>", views.AlbumUpdate.as_view(), name="album_update"),
    path("albums/delete/<int:pk>", views.AlbumDelete.as_view(), name="album_delete"),
    # SONGS MANAGEMENT API
    path("songs/create", views.SongCreate.as_view(), name="create_song"),
    path("songs/list", views.SongList.as_view(), name="song_list"),
    path("songs/detail/<int:pk>", views.SongDetail.as_view(), name="song_detail"),
    path("songs/update/<int:pk>", views.SongUpdate.as_view(), name="song_update"),
    path("songs/delete/<int:pk>", views.SongDelete.as_view(), name="song_delete"),

    path("songs/add_song_to_album", views.AddSongToAlbum.as_view(), name="add_song_to_album"),
]

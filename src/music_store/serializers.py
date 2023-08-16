from rest_framework import serializers

from src.music_store.models import Artist, Album, Song, SongsAndAlbums


class ArtistSerializer(serializers.ModelSerializer):
    # should be named same as Album model ForeignKey(related_name)
    albums = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    albums_count = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ('id', 'name', 'albums_count', 'albums')

    def get_albums_count(self, obj):
        return obj.albums.all().count()


class AlbumSerializer(serializers.ModelSerializer):
    # should be named same as Song model ForeignKey(related_name)
    songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    artist_name = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ('id', 'artist_name', 'year_created', 'songs')

    def get_artist_name(self, obj):
        return obj.artist.name


class SongsSerializer(serializers.ModelSerializer):
    # should be named same as Album model ForeignKey(related_name)
    albums = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    albums_count = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = ('id', 'title', 'albums_count', 'albums')

    def get_albums_count(self, obj):
        return obj.albums.all().count()


class SongsAndAlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = SongsAndAlbums
        fields = ("id", "album", 'song', 'song_number')
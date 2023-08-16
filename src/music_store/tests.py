import json

from django.contrib.auth import get_user_model
from django.test import Client
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from src.music_store.models import Artist
from src.music_store.serializers import ArtistSerializer

# initialize the APIClient app
client = Client()


class CreateNewArtistTest(TestCase):
    """Test module for sign up new artist API"""

    def setUp(self):
        self.valid_payload = {"name": "Olaf Stolke"}

        self.invalid_payload = {"name": ""}

    def test_create_valid_artist(self):
        response = client.post(
            reverse("create_artist"),
            data=json.dumps(self.valid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_artist(self):
        response = client.post(
            reverse("create_artist"),
            data=json.dumps(self.invalid_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetSingleArtistTest(TestCase):
    """Test module for GET single artist API"""

    def setUp(self):
        self.test_artist = Artist.objects.create(name="Vladimir Kuzmin")

    def test_get_valid_single_artist(self):
        response = client.get(
            reverse(
                "artist_detail", kwargs={"pk": self.test_artist.pk}))
        artist = Artist.objects.get(pk=self.test_artist.pk)
        serializer = ArtistSerializer(artist)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_artist(self):
        response = client.get(reverse("artist_detail", kwargs={"pk": 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class GetAllArtistsTest(TestCase):
    """Test module for GET all artists API"""

    def setUp(self):

        Artist.objects.create(name="Bon Jovie")
        Artist.objects.create(name="Ricki Martin")
        Artist.objects.create(name="Madonna")
        Artist.objects.create(name="Adel")

    def test_get_artist_list(self):
        # get API response
        response = client.get(reverse("artist_list"))
        # get data from db
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        self.assertEqual(Artist.objects.count(), 4)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class UpdateSingleUserTest(TestCase):
    """Test module for updating an existing artist record"""

    def setUp(self):
        self.test_artist = Artist.objects.create(name="Madonna")

        self.valid_put_payload = {"name": "Madona Renamed"}

        self.invalid_put_payload = {"name": ""}

    def test_valid_put_artist(self):
        response = client.put(
            reverse(
                "artist_update", kwargs={"pk": self.test_artist.pk}),
            data=json.dumps(self.valid_put_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_put_user(self):
        response = client.put(
            reverse("artist_update", kwargs={"pk": self.test_artist.pk}),
            data=json.dumps(self.invalid_put_payload),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleArtistTest(TestCase):
    """Test module for deleting an existing artist record"""

    def setUp(self):
        self.test_artist = Artist.objects.create(name="Bon Jovie")

    def test_valid_delete_artist(self):
        response = client.delete(
            reverse("artist_delete", kwargs={"pk": self.test_artist.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_artist(self):
        response = client.delete(reverse("artist_delete", kwargs={"pk": 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


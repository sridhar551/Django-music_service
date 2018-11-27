from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from .models import Songs
from .serializers import SongSerializer

# Create your tests here.

class BaseViewTest(APITestCase):
    client = APITestCase

    @staticmethod
    def create_song(title = "", artist=""):
        if title != "" and artist !="":
            Songs.objects.create(title=title, artist=artist)

    def setUp(self):
        self.create_song("like glue", "sean paul")
        self.create_song("simple song", "konshens")
        self.create_song("love is wicked", "brick and lace")
        self.create_song("jam rock", "demein marley")


class GetAllSongsTest(BaseViewTest):


    def test_get_all_songs(self):
        response = self.client.get(reverse("songs-all", kwargs={"version" : "v1"}))

        expected=Songs.objects.all()
        serialized = SongsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)




from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from BeerApp.views.beer_view import BeerViewSet
from BeerApp.utils.factory.user_factory import UserFactory

class TestBeerViewSet(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        UserFactory()

    def setUp(self) -> None:
        self.user = User.objects.all()[0]
        self.token = Token.objects.create(user = self.user)
        self.client = APIClient()

    def test_get_method_beer_api_url(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.get("/data/get_all_beers/")

        self.assertEqual(response.status_code, 200)

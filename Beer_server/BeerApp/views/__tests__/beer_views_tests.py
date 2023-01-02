from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from BeerApp.utils.factory.beer_factory import BeerFactory
from BeerApp.utils.factory.user_factory import UserFactory
from BeerApp.models.beer_model import Beer
from BeerApp.serializers.beer_serializers import BeerSerializer

class TestBeerViewSet(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        BeerFactory()
        UserFactory()

    def setUp(self) -> None:
        self.user = User.objects.all()[0]
        self.token = Token.objects.create(user = self.user)
        self.client = APIClient()

    def test_get_method_beer_api_response_data(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get("/data/get_all_beers/")

        response_data_expected = BeerSerializer(Beer.objects.all(), many=True)

        self.assertEqual(response.data, response_data_expected.data)

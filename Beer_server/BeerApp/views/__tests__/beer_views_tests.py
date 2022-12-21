from django.test import TestCase, RequestFactory
from django.urls import reverse
from rest_framework.test import APIRequestFactory
import json

from BeerApp.utils.factory.beer_factory import BeerFactory
from BeerApp.models.beer_model import Beer
from ..beer_view import BeerViewSet
from BeerApp.serializers.beer_serializers import BeerSerializer

class TestBeerViewSet(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        BeerFactory()

    def test_get_method_beer_api_url(self):
        factory_request = APIRequestFactory()
        view = BeerViewSet.as_view({'get': 'list'})

        request = factory_request.get("/data/get_all_beers/")
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_get_method_beer_api_response_data(self):
        factory_request = APIRequestFactory()
        view = BeerViewSet.as_view({'get': 'list'})

        request = factory_request.get("/data/get_all_beers/")
        response = view(request)

        response_data_expected = BeerSerializer(Beer.objects.all(), many=True)

        self.assertEqual(response.data, response_data_expected.data)

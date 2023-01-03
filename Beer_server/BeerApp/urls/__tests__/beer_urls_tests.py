from django.test import TestCase
from rest_framework.test import APIRequestFactory

from BeerApp.views.beer_view import BeerViewSet

class TestBeerViewSet(TestCase):
    def test_get_method_beer_api_url(self):
        factory_request = APIRequestFactory()
        view = BeerViewSet.as_view({'get': 'list'})

        request = factory_request.get("/data/get_all_beers/")
        response = view(request)
        self.assertEqual(response.status_code, 200)

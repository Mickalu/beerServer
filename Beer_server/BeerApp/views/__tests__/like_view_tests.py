from django.test import TestCase, RequestFactory
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import User

from BeerApp.models import Like, Beer
from BeerApp.views.like_view import LikeViewSet
from BeerApp.serializers.like_serializer import LikeSerializerReturnData
from BeerApp.utils.factory.beer_factory import BeerFactory
from BeerApp.utils.factory.like_factory import LikeFactory
from utils.API_utils.get_serializer_data import convert_ordeddirect_to_list
from utils.API_utils.class_reponse_api import Response_API

class TestLikeViewSet(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        for i in range(10): BeerFactory()

    def setUp(self) -> None:
        self.user = User.objects.create()
        self.token = Token.objects.create(user=self.user)

        for i in range(2): LikeFactory(user=self.user)

    def test_get_user_likes_list(self):

        factory = APIRequestFactory(
            content_type="application/json",
        ).get("beer/get-likes/", HTTP_AUTHORIZATION='Token {}'.format(self.token.key))

        viewSet_get_user_beers = LikeViewSet.as_view({'get': 'list'})
        response = viewSet_get_user_beers(factory)

        queryset_user_likes = Like.objects.filter(user=self.user)
        serializer_data = LikeSerializerReturnData(queryset_user_likes, many=True).data
        response_api = Response_API(status=True, data= convert_ordeddirect_to_list(serializer_data, 'beer'))

        message_expected = response_api.__dict__

        self.assertEqual(response.data, message_expected)

    def test_create_like(self):
        beers_liked = Like.objects.filter(user=self.user).values_list("beer", flat=True)
        beer_id = Beer.objects.all().exclude(pk__in=beers_liked)[0].id

        data = {
            'beer': beer_id
        }

        factory = APIRequestFactory(
            content_type = "application/json",
        ).post("beer/create-like/", data, HTTP_AUTHORIZATION='Token {}'.format(self.token.key), format='json')

        view_create = LikeViewSet.as_view({'post': 'create'})
        response = view_create(factory)

        beers_liked_updated = Like.objects.filter(user=self.user).values_list("beer", flat=True)

        self.assertEqual(response.data['status'], True)
        self.assertEqual(response.data['data']['user'], self.user.id)
        self.assertTrue(response.data['data']['beer'] in beers_liked_updated)

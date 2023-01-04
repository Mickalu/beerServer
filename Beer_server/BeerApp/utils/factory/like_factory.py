import factory

from BeerApp.models.like_model import Like
from BeerApp.utils.factory.user_factory import UserFactory
from BeerApp.utils.factory.beer_factory import BeerFactory

class LikeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Like

    user = factory.SubFactory(UserFactory)
    beer = factory.SubFactory(BeerFactory)

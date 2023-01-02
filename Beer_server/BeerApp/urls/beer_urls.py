from rest_framework import routers

from ..views import BeerViewSet

app_name = "beer_api"

router = routers.DefaultRouter()
router.register("get_all_beers", BeerViewSet, basename="beers")

from rest_framework import routers

from ..views import BeerViewSet

router = routers.DefaultRouter()
router.register("get_all_beers", BeerViewSet)

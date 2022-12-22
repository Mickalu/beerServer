from rest_framework import routers

from Authentification.views import UserViewSet

app_name = "authentification_user"
router = routers.DefaultRouter()
router.register("registration_user", UserViewSet, basename='User')

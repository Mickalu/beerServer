"""Beer_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from BeerApp.urls.beer_urls import router as beer_router
from Authentification.urls.user_urls import router as user_registration_router

router = routers.DefaultRouter()
router.registry.extend(beer_router.registry)
router.registry.extend(user_registration_router.registry)

app_name = "app_server"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("data/", include(router.urls)),
    path("user/", include(user_registration_router.urls)),
]

urlpatterns += user_registration_router.urls

from django.urls import path

from BeerApp.views.like_view import LikeViewSet

urlpatterns = [
  path('create-like/', LikeViewSet.as_view({'post': 'create'}), name='create-like'),
  path('get-likes/', LikeViewSet.as_view({'get': 'list'}), name='get-likes'),
]

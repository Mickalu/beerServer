from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..serializers import BeerSerializer
from ..models import Beer

class BeerViewSet(viewsets.ModelViewSet):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer

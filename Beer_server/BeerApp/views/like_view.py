from rest_framework import viewsets, status
from rest_framework.response import Response
import json

from BeerApp.serializers import LikeSerializer, LikeSerializerReturnData
from BeerApp.models import Like
from utils.API_utils.class_reponse_api import Response_API
from utils.API_utils.token_utils import get_user_by_token_headers

class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer

    def list(self, request):
        try:
            user = get_user_by_token_headers(request)

            queryset = Like.objects.filter(user=user)
            serializer_data = LikeSerializerReturnData(queryset, many=True).data

            return Response(serializer_data, status=status.HTTP_201_CREATED)

        except Exception:
            return Response(Exception, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        user = get_user_by_token_headers(request)
        data_from_request = request.data.dict()
        data_from_request["user"] = user.id

        serializer = LikeSerializer(data=data_from_request)
        response_api = Response_API()

        if serializer.is_valid():
            serializer.save()
            response_api.status = True
            response_api.data = serializer.data

            return Response(response_api.__dict__, status=status.HTTP_201_CREATED)

        else:
            response_api.status = False
            response_api.data = serializer.errors

            return Response(response_api.__dict__, status=status.HTTP_400_BAD_REQUEST)

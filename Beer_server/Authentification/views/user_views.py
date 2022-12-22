from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
import json

from utils.API_utils.class_reponse_api import Response_API
from Authentification.serializers.user_serializer import UserSerilizer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerilizer

    def get_queryset(self) -> User:
        user = self.request.user

    def create(self, request ) -> None:
        serializer = UserSerilizer(data=request.data)
        response_api = Response_API()

        if serializer.is_valid():
            serializer.save()
            response_api.status = True
            response_api.data = serializer.data
            return Response(json.dumps(response_api.__dict__), status=status.HTTP_201_CREATED)

        else:
            response_api.status = False
            response_api.data = serializer.errors
            return Response(json.dumps(response_api.__dict__), status=status.HTTP_400_BAD_REQUEST)


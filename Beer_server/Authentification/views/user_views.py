from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from Authentification.serializers.user_serializer import UserSerilizer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerilizer

    def get_queryset(self) -> User:
        user = self.request.user

    def create(self, request ) -> None:
        serializer = UserSerilizer(data=request.data)

        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


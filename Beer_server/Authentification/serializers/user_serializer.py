from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerilizer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, style={'input_type': 'password', 'placeholder': 'Password'})

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password")

    def create(self, validated_data) -> User:
        user = User.objects.create(
           username = validated_data.pop("username"),
           email = validated_data.pop("email"),
           first_name = validated_data.pop("first_name"),
           last_name = validated_data.pop("last_name"),
        )

        user.set_password(validated_data.pop("password"))
        user.save()

        return user

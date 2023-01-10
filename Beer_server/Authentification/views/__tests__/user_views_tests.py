from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import User

from Authentification.views.user_views import UserViewSet

class TestCreationUser(TestCase):
    def test_post_method_user_creation(self):
        post_formdata = {
            "username": "dev",
            "first_name": "test",
            "last_name": "test",
            "password": "password",
            "email": "test@gmail.com",
        }

        self.client.post("/user/registration_user/", post_formdata, format="json")
        nbr_users = len(User.objects.all())

        self.assertEqual(nbr_users, 1)

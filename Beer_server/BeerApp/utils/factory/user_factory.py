from django.contrib.auth.models import User
import factory

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "username {}".format(n))
    first_name = factory.Sequence(lambda n: "first_name {}".format(n))
    last_name = factory.Sequence(lambda n: "last_name {}".format(n))
    email = factory.Sequence(lambda n: "emailTest{}@gmail.com".format(n))
    password = "password"

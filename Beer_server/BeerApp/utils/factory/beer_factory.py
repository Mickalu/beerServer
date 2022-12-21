from BeerApp.models.beer_model import Beer
import factory

class BeerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Beer

    title = factory.Sequence(lambda n: "title beer {}".format(n))
    description = factory.Sequence(lambda n: "description beer {}".format(n))
    country = factory.Faker("country")
    type_beer = factory.Sequence(lambda n: "type beer {}".format(n))
    company = factory.Faker("company")
    colour = factory.Faker("color_name")
    graduation = factory.Faker("random_int", min=0, max=100)
    size = factory.Faker("random_int", min=0, max=100)
    price = factory.Faker("random_int", min = 0)
    photo_link = factory.Faker("image_url")

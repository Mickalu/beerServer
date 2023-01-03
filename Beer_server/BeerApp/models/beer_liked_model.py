from django.db import models
from django.contrib.auth.models import User

from BeerApp.models import Beer

class LikedBeer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{} {}".format(self.user, self.beer)

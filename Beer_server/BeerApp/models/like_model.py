from django.db import models
from django.contrib.auth.models import User

from BeerApp.models import Beer

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'beer'),)

    def __str__(self) -> str:
        return "{} {}".format(self.user, self.beer)

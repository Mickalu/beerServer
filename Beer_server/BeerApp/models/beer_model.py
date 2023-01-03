from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Beer(models.Model):
    title = models.CharField(default="", max_length=150)
    description = models.TextField(default="")
    country = models.CharField(default="", max_length=150)
    type_beer = models.CharField(default="", max_length=150)
    company = models.CharField(default="", max_length=150)
    colour = models.CharField(default="", max_length=150)
    graduation = models.FloatField(default=0.0)
    size = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0,)
    photo_link = models.CharField(default="", max_length=200)

    def clean(self) -> None:
        if self.graduation < 0 or self.graduation > 100:
            raise ValidationError({'error': 'graduation is greater than 100 or less than 0'})

        if self.price < 0:
            raise ValidationError({'error': 'price is less than 0'})

        if self.size < 0:
           raise ValidationError({'error': 'size is less than 0'})

    def __str__(self) -> str:
        return self.title

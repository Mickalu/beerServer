# Generated by Django 4.1.4 on 2023-01-03 16:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("BeerApp", "0002_beerliked"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="BeerLiked",
            new_name="LikedBeer",
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-04 07:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("BeerApp", "0004_alter_likedbeer_unique_together"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="LikedBeer",
            new_name="Like",
        ),
    ]
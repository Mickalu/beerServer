from django.contrib import admin
from .models import Beer, LikedBeer

# Register your models here.
admin.site.register(Beer)
admin.site.register(LikedBeer)

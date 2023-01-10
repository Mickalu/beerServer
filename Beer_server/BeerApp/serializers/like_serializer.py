from rest_framework import serializers

from BeerApp.models import Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('user', 'beer')

class LikeSerializerReturnData(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('beer',)

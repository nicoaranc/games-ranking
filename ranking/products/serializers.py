from rest_framework import serializers
from .models import Game, Platform, Image

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('id', 'name', 'platform', 'score', 'get_image', 'get_thumbnail')

class PlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = Platform
        fields = ('name')

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('route', 'game')
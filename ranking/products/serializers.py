from rest_framework import serializers
from .models import Game, Platform, Image

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('id', 
                  'name', 
                  'platform', 
                  'score',
                  'get_absolute_url',
                  'get_image', 
                  'get_thumbnail', 
                  'description', 
                  'video',
                  'slug',
                  'image')

class PlatformSerializer(serializers.ModelSerializer):
    games = GameSerializer(many=True)

    class Meta:
        model = Platform
        fields = ('name', 
                  'slug', 
                  'name_desc', 
                  'games')

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('route', 'game')
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Game, Platform, Image
from .serializers import GameSerializer, PlatformSerializer, ImageSerializer

from django.http import Http404

# Create your views here.

class GameList(APIView):
    def get(self, request, format=None):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

class GameDetail(APIView):
    def get_object(self, platform_slug, game_slug):
        try:
            return Game.objects.filter(platform__slug=platform_slug).get(slug=game_slug)
        except Game.DoesNotExist:
            raise Http404
    
    def get(self,request, platform_slug, game_slug, format=None):
        game = self.get_object(platform_slug, game_slug)
        serializer = GameSerializer(game)
        return Response(serializer.data)

class PlatformList(generics.ListCreateAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class PlatformDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
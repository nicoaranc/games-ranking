from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Game, Platform
from .serializers import GameSerializer, PlatformSerializer

from django.http import Http404, QueryDict

# Create your views here.

class GameList(APIView):
    def get(self, request, format=None):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        
        print(request.data)

        serializer = GameSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'mensaje': 'Solicitud POST recibida'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

class PlatformList(APIView):
    def get(self, request, format=None):
        platforms = Platform.objects.all()
        serializer = PlatformSerializer(platforms, many=True)
        return Response(serializer.data)

class PlatformDetail(APIView):
    def get_object(self, platform_slug):
        try:
            return Platform.objects.get(slug=platform_slug)
        except Game.DoesNotExist:
            raise Http404
        
    def get(self, request, platform_slug, format=None):
        platform = self.get_object(platform_slug)
        serializer = PlatformSerializer(platform)
        return Response(serializer.data)

from django.urls import path
from .views import *

urlpatterns = [
    path('games/', GameList.as_view(), name='game-list'),
    path('games/<slug:platform_slug>/<slug:game_slug>/', GameDetail.as_view(), name='game-detail'),
    path('platforms/', PlatformList.as_view(), name='platform-list')
]
from django.urls import path
from .views import *

urlpatterns = [
    path('games/', GameList.as_view(), name='game-list'),
    path('games/<int:pk>', GameDetail.as_view(), name='game-detail'),
]
from django.urls import path
from . import views
from .views import GameListView

urlpatterns = [
    path('', views.home, name='game-home'),
    path('new/', views.new, name='game-create'),
    path('about/', views.about, name='game-about'),
    path('games_history/', GameListView.as_view(), name='game-list'),
]

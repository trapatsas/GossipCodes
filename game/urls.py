from django.urls import path
from . import views
from .views import GameListView, SessionDetailView, PlayerAliasCreateView, session_create

urlpatterns = [
    path('', views.home, name='game-home'),
    path('new/', session_create, name='game-create'),
    # path('game_new/', SessionCreateView.as_view(), name='game-create2'),
    path('game/<str:pk>/', SessionDetailView.as_view(), name='game-session'),
    path('about/', views.about, name='game-about'),
    path('games_history/', GameListView.as_view(), name='game-list'),
]

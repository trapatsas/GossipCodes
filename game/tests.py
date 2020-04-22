from django.test import TestCase

from django.contrib.auth.models import User

# Create your tests here.
from game.models import GameSession, GameStatus, PlayerAlias

s1 = GameSession(
    session_url='a12345',
    status=GameStatus.NEW,
    host=User.objects.first(),
    random_word='abracatabra'
)

s1.save()

p1 = PlayerAlias(
    player=User.objects.first(),
    alias='Player £1',
    game_session=s1,
)

p1.save()

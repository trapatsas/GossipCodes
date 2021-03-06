import random
import string
from enum import Enum

from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.

def genpk():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))


class PlayerRole(Enum):
    GAME_MASTER = "Game Master"
    SPY = "Spy"
    NORMAL = "Player"


class GameResult(Enum):
    GAME_MASTER_WINS = "Word not found"
    SPY_LOSES = "Spy discovered"
    SPY_WINS = "Spy wins"


class GameStatus(Enum):
    NEW = "New"
    ACTIVE = "Active"
    COMPLETED = "Finished"
    ABANDONED = "Abandoned"
    PAUSED = "Paused"
    CANCELLED = "Exited"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __repr__(self):
        return self.user.username

    def __str__(self):
        return f'{self.user.username} Profile'


class GameSession(models.Model):
    game_code = models.CharField(max_length=5, primary_key=True, default=genpk)
    status = models.CharField(max_length=25, choices=[(tag.name, tag.value) for tag in GameStatus], null=False,
                              default=GameStatus.NEW)
    host = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, null=False)
    # tournament = models.ForeignKey(Tournament, on_delete=models.DO_NOTHING, null=True)
    random_word = models.CharField(max_length=42, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(default=None, null=True)
    result = models.CharField(max_length=25, choices=[(tag.name, tag.value) for tag in GameResult], null=True)

    def __repr__(self):
        return self.game_code

    def __str__(self):
        return f'Game #{self.game_code}'

    def get_absolute_url(self):
        return reverse('game-session', kwargs={'pk': self.pk})


class PlayerAlias(models.Model):
    player = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, null=False)
    game_session = models.ForeignKey(GameSession, on_delete=models.DO_NOTHING, null=False)
    role = models.CharField(max_length=25, choices=[(tag.name, tag.value) for tag in PlayerRole], null=True)
    alias = models.CharField(max_length=15, null=False, help_text='Choose a nickname')
    points_earned = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('player', 'game_session')

    def __repr__(self):
        return self.alias

    def __str__(self):
        return self.alias

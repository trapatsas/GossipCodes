from django.contrib import admin
from .models import GameSession, PlayerAlias, Profile


# Register your models here.
@admin.register(GameSession)
class GameSessionAdmin(admin.ModelAdmin):
    list_display = ('random_word', 'game_code')


@admin.register(PlayerAlias)
class PlayerAliasAdmin(admin.ModelAdmin):
    list_display = ('player', 'game_session', 'role', 'alias')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

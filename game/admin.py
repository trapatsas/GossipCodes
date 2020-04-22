from django.contrib import admin
from .models import GameSession, PlayerAlias, Profile


# Register your models here.
@admin.register(GameSession)
class GameSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'random_word', 'session_url')


@admin.register(PlayerAlias)
class PlayerAliasAdmin(admin.ModelAdmin):
    list_display = ('player', 'role', 'alias')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

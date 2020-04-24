from pprint import pprint

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages

from .forms import NewPlayerAliasForm, JoinGameForm
from .models import GameSession, PlayerAlias


# Create your views here.

@login_required
def home(request):
    if request.method == 'POST':
        form = JoinGameForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            game_code = cd.get('gcode')
            alias = cd.get('alias')
            try:
                game = GameSession.objects.filter(game_code=game_code).first()
                alias_obj = PlayerAlias(alias=alias, game_session=game, player=request.user.profile)
                alias_obj.save()
                messages.success(request, f'You joined the game!')
            except IntegrityError as e:
                messages.warning(request, f'User has already joined!')
                return render(request, 'home.html')
            return redirect('game-session', pk=game_code)
        else:
            messages.warning(request, f'Invalid Game Code!')
    return render(request, 'home.html')


class GameListView(LoginRequiredMixin, ListView):
    model = GameSession
    template_name = 'games.html'
    context_object_name = 'sessions'
    ordering = ['-created_at']


class SessionDetailView(LoginRequiredMixin, DetailView):
    model = GameSession
    template_name = 'session.html'
    context_object_name = 'game_session'


# class SessionCreateView(LoginRequiredMixin, CreateView):
#     model = GameSession
#     template_name = 'new.html'
#     fields = ['random_word', 'game_code', 'status']
#
#     def form_valid(self, form):
#         form.instance.host = self.request.user.profile
#         return super().form_valid(form)


class PlayerAliasCreateView(LoginRequiredMixin, CreateView):
    model = PlayerAlias
    template_name = 'new.html'
    fields = ['alias']

    def form_valid(self, form):
        form.instance.player = self.request.user.profile
        return super().form_valid(form)


@login_required
def game_start(request):
    if request.method == 'POST':
        alias_form = NewPlayerAliasForm(request.POST)
        alias_form.instance.player = request.user.profile
        new_game = GameSession(host=request.user.profile)
        alias_form.instance.game_session = new_game

        if alias_form.is_valid():
            new_game.save()
            alias_form.save()
            messages.success(request, f'Game with code {new_game.game_code} has been created!')
            return redirect('game-session', pk=new_game.game_code)
    else:
        alias_form = NewPlayerAliasForm(initial={'alias': request.user.username})

    context = {
        'players': alias_form,
        'title': 'New Game'
    }
    return render(request, 'lobby.html', context)


@login_required
def session_create(request):
    if request.method == 'POST':
        alias_form = NewPlayerAliasForm(request.POST)
        alias_form.instance.player = request.user.profile
        new_game = GameSession(host=request.user.profile)
        alias_form.instance.game_session = new_game

        if alias_form.is_valid():
            new_game.save()
            alias_form.save()
            messages.success(request, f'Game with code {new_game.game_code} has been created!')
            return redirect('game-session', pk=new_game.game_code)
    else:
        alias_form = NewPlayerAliasForm(initial={'alias': request.user.username})

    context = {
        'alias_form': alias_form,
        'title': 'New Game'
    }
    return render(request, 'new.html', context)


# @login_required
# def session_create(request):
#     if request.method == 'POST':
#         alias_form = NewPlayerAliasForm(request.POST, instance=request.user.profile.playeralias_set.first)
#         alias_form.instance.player = request.user.profile
#         alias_form.instance.game_session =
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Account has been updated!')
#             return redirect('profile')
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#
#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }
#     return render(request, 'profile.html', context)


@login_required
def all_games(request):
    context = {
        'sessions': GameSession.objects.all(),
        'title': 'All games'
    }
    return render(request, 'games.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About'})


@login_required
def new(request):
    return render(request, 'new.html', {'title': 'Create New Game'})

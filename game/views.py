from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import GameSession


# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')


# @login_required
class GameListView(ListView):
    model = GameSession
    template_name = 'games.html'
    context_object_name = 'sessions'


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

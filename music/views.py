from django.shortcuts import render

from controller.models import Que


def home(request):
    return render(request, "music/home.html")


def player(request):
    que = Que.objects.last()
    context = {
        "que": que
    }
    return render(request, "music/player.html", context)

from django.shortcuts import render


def home(request):
    return render(request, "music/home.html")


def player(request):
    return render(request, "music/player.html")

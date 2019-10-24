from . import pygame_wrapper as pw

from django.http import HttpResponseRedirect

from .models import Que
from music.models import Playlist

# todo: make it an API
def play(request):
    que_id = request.POST.get('que_id', False)
    que = Que.objects.get(id=que_id)
    import pdb; pdb.set_trace()

    if not que.active:
        # activate que
        p = pw.Pygame()
        que.active = True
        que.save(update_fields=["active"])
        # fetch playlist

        # que.playlist
    # if que.status ==
    # todo: take que, fetch all the songs, init pygame, que the songs and play
    # todo: than change que to active and redirect to previous page
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

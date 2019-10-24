from Cirify import tasks as t

from django.http import HttpResponseRedirect

from .models import Que
from music.models import Playlist


# todo: make it an API
def play(request):
    que_id = request.POST.get('que_id', False)
    que = Que.objects.get(id=que_id)
    # import pdb; pdb.set_trace()
    if True:
    # if not que.active and que.status == 'Ready':
        # activate que
        # todo: django fails here - needs to be handled in Celery
        from controller import pygame_wrapper as pw
        t.test_task.delay()
        # import pdb; pdb.set_trace()
        pygame = t.init.delay()
        que.active = True
        que.save(update_fields=["active"])
        song = que.playlist.songs.first().location
        # t.play.delay(song, pygame)
        que.status = 'Playing'
        que.save(update_fields=["status"])
        # fetch playlist and que songs
        # for song in que.playlist.songs.only('location').iterator():
        #     p.queue(song)
        # p.play()
    # todo: take que, fetch all the songs, init pygame, que the songs and play
    # todo: than change que to active and redirect to previous page
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


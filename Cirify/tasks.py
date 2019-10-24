from celery import shared_task
from controller import pygame_wrapper as pw


@shared_task
def test_task():
    print("CELERY: test-task ---- -esfsdfsdfs -------")


@shared_task
def init():
    print("CELERY: INFO---- INITIALIZING PYGAME -------")
    return pw.Pygame()


@shared_task
def play(file, pygame):
    import pdb; pdb.set_trace()
    return pygame.play(file)

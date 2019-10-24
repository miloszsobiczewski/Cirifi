from celery import shared_task
from . import pygame_wrapper as pw


@shared_task
def init():
    return pw.Pygame()

@shared_task
def play(file):



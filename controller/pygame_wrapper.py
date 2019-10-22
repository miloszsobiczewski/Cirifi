import pygame


class Pygame():
    """
    Wrapper for Pygame
    https://www.pygame.org/docs/ref/music.html#module-pygame.mixer.music
    """
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

    def load(self, file):
        pygame.mixer.music.load(file)

    def play(self):
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()

    def rewind(self):
        pygame.mixer.music.rewind()

    def fadeout(self):
        pygame.mixer.music.fadeout()

    def set_volume(self):
        pygame.mixer.music.set_volume()

    def get_volume(self):
        pygame.mixer.music.get_volume()

    def queue(self):
        pygame.mixer.music.queue()

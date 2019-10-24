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

    def play(self, loops=0, start=0.0):
        pygame.mixer.music.play(loops, start)

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()

    def rewind(self):
        pygame.mixer.music.rewind()

    def fadeout(self, time):
        pygame.mixer.music.fadeout(time)

    def set_volume(self, value):
        """
        set value between 0.0 and 1.0
        """
        pygame.mixer.music.set_volume(value)

    def get_volume(self):
        pygame.mixer.music.get_volume()

    def queue(self, file):
        pygame.mixer.music.queue(file)

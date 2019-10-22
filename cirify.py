import pygame
file = 'file_example_MP3_1MG.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
m = pygame.mixer.music.play()
# pygame.event.wait()  # to play all
import pdb;

pdb.set_trace()
# pygame.mixer.pause
# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)
#     import pdb; pdb.set_trace()

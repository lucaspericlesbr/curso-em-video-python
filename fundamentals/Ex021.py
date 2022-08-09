'''Make a python program that opens and plays audio from an mp3 file.'''

import pygame

pygame.init()
pygame.mixer.music.load('Ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

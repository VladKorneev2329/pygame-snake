import pygame
from mainParametrs import *
from checkEvent import check_event

pygame.init()
pygame.display.set_mode(display_size)
pygame.display.set_caption(display_title)

while True:

    check_event()

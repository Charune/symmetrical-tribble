import pygame
from settings import RectSettings, SeasonSettings, Master

pygame.init()

#Game Caption
pygame.display.set_caption("Racket Sim")

#Set Game Loop
done = False

#Pygame Clock
clock = pygame.time.Clock()

#Initialize RectSettings object to pass details of Rects
rectSettings = RectSettings()
seasonSettings = SeasonSettings()
#Initialize Master object to maintain game state.
master = Master(rectSettings)

import pygame
import settings
import buttons
import scenes
import json

pygame.init()

#Game Caption
pygame.display.set_caption("Racket Sim")

#Set Game Loop
done = False

#Pygame Clock
clock = pygame.time.Clock()

#Initialize Master object to maintain game state.
master = settings.Master()

#Initialize RectSettings object to pass details of Rects
rectSettings = settings.RectSettings()

#Unpack the button and scene JSON into objects.
buttons.unpackButtons(json.buttonJSON, buttons.buttonDict, rectSettings)
scenes.unpackScene(json.sceneJSON, scenes.sceneDict)

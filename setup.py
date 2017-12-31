import pygame
from  settings import RectSettings, Master
import sceneObjects2
import teammates
import json

pygame.init()

#Game Caption
pygame.display.set_caption("Racket Sim")

#Set Game Loop
done = False

#Pygame Clock
clock = pygame.time.Clock()

#Initialize RectSettings object to pass details of Rects
rectSettings = RectSettings()
#Initialize Master object to maintain game state.
master = Master(rectSettings)

'''
#Initialize Master object to maintain game state.
master = settings.Master()

#Initialize RectSettings object to pass details of Rects
rectSettings = settings.RectSettings()

#Unpack the button and scene JSON into objects.
#sceneObjects.unpackButtons(json.buttonJSON, sceneObjects.buttonDict, rectSettings)
#sceneObjects.unpackButtons(json.buttonList, sceneObjects.buttonDict, rectSettings)
#sceneObjects.unpackScene(json.sceneJSON, sceneObjects.sceneDict)
#sceneObjects.unpackScene(json.sceneList, sceneObjects.sceneDict)
#teammates.unpackTeammates(teammates.teammatesJSON, teammates.teammateDict)
'''

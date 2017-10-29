#####
# v. 0.0.2
# 10/07/2017
#####

from setup import master, clock, done, rectSettings
import pygame
from sceneObjects import sceneDict
from event import eventQueue

while not done:
    #Draw current scene
    sceneDict[master.sceneId].drawScene(rectSettings, master)

    #run event and end if user quits
    done = eventQueue()

    sceneDict[master.sceneId].update(rectSettings, master)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

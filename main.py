#####
# v. 0.0.1
# 10/07/2017
#####

from setup import master, clock, done, rectSettings
import pygame
from scenes import sceneDict
from event import eventQueue

while not done:
    sceneDict[master.sceneId].draw(rectSettings)

    done = eventQueue()

    sceneDict[master.sceneId].update(master)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

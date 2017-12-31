#####
# v. 0.0.3
# 11/06/2017
#####

from setup import master, clock, done, rectSettings
import pygame
from event import eventQueue

while not done:
    #Draw current scene.
    master.sceneDict[master.sceneId].drawScene(rectSettings, master)
    #run event and end if user quits.
    done = eventQueue()

    master.sceneDict[master.sceneId].update(master)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

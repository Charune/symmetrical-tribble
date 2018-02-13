#####
# v. 0.0.4
# 01/07/2018
#####

from setup import master, clock, done, rectSettings
import pygame
from event import eventQueue

while not done:
    #Draw current scene.
    master.sceneDict[master.sceneId].drawScene(rectSettings, master)
    #Run event and end if user quits.
    done = eventQueue()
    #Update current scene.
    master.sceneDict[master.sceneId].update(master, rectSettings)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

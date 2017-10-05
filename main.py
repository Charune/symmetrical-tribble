#####
# v. 0.0.01
# 9/25/2017
#####

import pygame
import settings
import buttons
import scenes
import json

pygame.init()
pygame.display.set_caption("Racket Sim")
#background = pygame.image.load(r'Art\SoftTennis3Scaled.png')

done = False
clock = pygame.time.Clock()

rectSettings = settings.RectSettings()
rectSettings.screen.fill(rectSettings.BLACK)
master = settings.Master()

screenNavigator = 0

buttons.unpackButtons(json.buttonJSON, buttons.buttonDict, rectSettings)
scenes.unpackScene(json.sceneJSON, scenes.sceneDict)

while not done:
    scenes.sceneDict[master.sceneId].draw(rectSettings)
    #rectSettings.screen.blit(rectSettings.messageRectFill,(0,0)) #TODO: Change to generic blackRectFill at somepoint
    #rectSettings.screen.blit(background,(0,0))

    #if(screenNavigator == 0):
        #buttons.drawButton(rectSettings, 'Start', rectSettings.screenRect.center)
        #buttons.buttonDict['Start'].draw(rectSettings)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            master.mousePos = pygame.mouse.get_pos()

    scenes.sceneDict[master.sceneId].update(master)
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #mousePos = pygame.mouse.get_pos()
            #if(screenNavigator == 0):
                #if(buttons.pressed(rectSettings.startButtonRect, mousePos)):
                     #pass
        #         if(pressed(lobRect, mousePos)):
        #             pM.lob(athlete1)
        #     elif(pM.progress == 2):
        #         if(pressed(screenRect,mousePos)):
        #             pM.progress = 3
        #     elif(pM.progress == 4):
        #         if(pressed(screenRect,mousePos)):
        #             pM.progress = 1
        #     elif(pM.progress == 9):
        #         if(pressed(retryRect,mousePos)):
        #             pM = PowerMeter()



    #buttons.drawMessage(rectSettings, "test")
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

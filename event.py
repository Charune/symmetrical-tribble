import pygame
from setup import done, master

#Receive event inputs from player
def eventQueue():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            return done
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            master.mousePos = pygame.mouse.get_pos()

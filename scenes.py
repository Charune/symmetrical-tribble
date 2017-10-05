from buttons import buttonDict
import pygame

pygame.init()

sceneDict = {}
def unpackScene(JSON, sceneDict):
    for scn in JSON:
        sceneDict[scn['id']]= Scene(scn)

class Scene():
    def __init__(self,JSON):
        self.id = JSON['id']
        self.buttons = []
        self.titleCard = JSON['titleCard']
        for btn in JSON['buttons']:
            self.buttons.append(buttonDict[btn])
        #self.background = JSON['background']
        if JSON['background'] == 'NULL':
            self.background = 'NULL'
        else:

            self.background = pygame.image.load(JSON['background'])
        #self.background = JSON['background']

    def update(self, master):
        for btn in self.buttons:
            btn.update(master)
        master.mousePos = None
        #updatebuttons


    def draw(self, settings):
        if self.background == 'NULL':
            settings.screen.blit(settings.screenRectFill,(0,0))
            drawTitleCard(settings, self.titleCard)
        else:
            settings.screen.blit(self.background,(0,0))
        for i, btn in enumerate(self.buttons):
            #btn.draw(settings)
            btn.drawSet(settings, i)

def drawTitleCard(rectSettings,text):
    #pygame.draw.rect(rectSettings.screen, rectSettings.BLACK, rectSettings.messageRect,1)
    messageText = rectSettings.font.render(text, True, rectSettings.WHITE)
    messageRect = pygame.Rect(400,40,0,0)#messageText.get_rect()
    textSurf = scaleMessage(rectSettings, messageRect, messageText)
    #rectSettings.screen.blit(rectSettings.messageRectFill, rectSettings.messageRect)
    rectSettings.screen.blit(messageText, textSurf)

def scaleMessage(rectSettings, messageRect, messageText):
    messageTextWidth = messageRect.centerx - messageText.get_width() / 2 #Need to change messageRect to an arguement
    messageTextHeight = messageRect.centery - messageText.get_height() / 2
    textSurf = [messageTextWidth, messageTextHeight]
    return textSurf

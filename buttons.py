import pygame

pygame.init()

buttonDict = {}
def unpackButtons(JSON, buttonDict, settings):
    for butn in JSON:
        buttonDict[butn['title']] = Button(butn, settings)

def scaleMessage(rectSettings, messageRect, messageText):
    messageTextWidth = messageRect.centerx - messageText.get_width() / 2 #Need to change messageRect to an arguement
    messageTextHeight = messageRect.centery - messageText.get_height() / 2
    textSurf = [messageTextWidth, messageTextHeight]
    return textSurf

def drawMessage(rectSettings,text):
    pygame.draw.rect(rectSettings.screen, rectSettings.BLACK, rectSettings.messageRect,1)
    messageText = rectSettings.font.render(text, True, rectSettings.WHITE)
    textSurf = scaleMessage(rectSettings, messageText)
    rectSettings.screen.blit(rectSettings.messageRectFill, rectSettings.messageRect)
    rectSettings.screen.blit(messageText, textSurf)



def pressed(rect, mousePos):
    if mousePos[0] > rect.topleft[0]:
        if mousePos[1] > rect.topleft[1]:
            if mousePos[0] < rect.bottomright[0]:
                if mousePos[1] < rect.bottomright[1]:
                    return True
    else: return False

class Button():
    def __init__(self,JSON, settings):
        self.title = JSON['title']
        self.actionType = JSON['actionType']
        self.actionValue = JSON['actionValue']
        self.center = JSON['center']
        self.rect = pygame.Rect((0,0), (0,0))
        self.rect.center = self.center
        self.rect.size = settings.buttonSize

    def draw(self,settings):
        buttonRectFill = settings.screen.subsurface(self.rect).convert_alpha()
        buttonRectFill.fill(settings.WHITE)
        pygame.draw.rect(settings.screen, settings.BLACK, self.rect,1)
        fontDetails = settings.font.render(self.title, True, settings.BLACK)
        textSurf = scaleMessage(settings, self.rect, fontDetails)
        settings.screen.blit(buttonRectFill, self.rect)
        settings.screen.blit(fontDetails, textSurf)

    def drawSet(self,settings, count):
        #
        btnRect = pygame.Rect(settings.buttonSetPos.topleft, settings.buttonSetPos.size)
        btnRect.y = settings.buttonSetPos.y + count*(settings.buttonSize[1] + settings.buttonSetGap)
        self.rect = btnRect
        buttonRectFill = settings.screen.subsurface(btnRect).convert_alpha()
        buttonRectFill.fill(settings.WHITE)
        pygame.draw.rect(settings.screen, settings.BLACK, btnRect,1)
        fontDetails = settings.font.render(self.title, True, settings.BLACK)
        textSurf = scaleMessage(settings, btnRect, fontDetails)
        settings.screen.blit(buttonRectFill, btnRect)
        settings.screen.blit(fontDetails, textSurf)

    def update(self, master):
        if master.mousePos != None:
            if self.rect.collidepoint(master.mousePos):
                self.click(master)


    def click(self, master):
        master.sceneId = self.actionValue

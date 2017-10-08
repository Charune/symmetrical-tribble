from buttons import buttonDict, scaleMessage
import pygame

#Dictionary of all scene objects
sceneDict = {}

#Convert JSON into scene objects and fill sceneDict
def unpackScene(JSON, sceneDict):
    for scn in JSON:
        sceneDict[scn['id']]= Scene(scn)

#An object that determines the present background/buttons for the player
class Scene():
    def __init__(self,JSON):
        self.id = JSON['id']
        self.buttons = []
        self.titleCard = JSON['titleCard']
        for btn in JSON['buttons']:
            self.buttons.append(buttonDict[btn])
        if JSON['background'] == 'NULL':
            self.background = 'NULL'
        else:
            self.background = pygame.image.load(JSON['background'])

    def update(self, master):
        for btn in self.buttons:
            btn.update(master)
        master.mousePos = None

    def draw(self, settings):
        if self.background == 'NULL':
            settings.screen.blit(settings.screenRectFill,(0,0))
            drawTitleCard(settings, self.titleCard)
        else:
            settings.screen.blit(self.background,(0,0))
        for i, btn in enumerate(self.buttons):
            btn.drawSet(settings, i)

def drawTitleCard(rectSettings,text):
    messageText = rectSettings.font.render(text, True, rectSettings.WHITE)
    messageRect = pygame.Rect(400,40,0,0)
    textSurf = scaleMessage(rectSettings, messageRect, messageText)
    rectSettings.screen.blit(messageText, textSurf)

sceneDict = {}
def unpackScene(JSON, sceneDict):
    for scn in JSON:
        sceneDict[scn.id]= Scene(scn)

buttonDict = {}
def unpackButtons(JSON, buttonDict):
    for butn in JSON:
        buttonDict[button.id] = Button(butn)

class Scene():
    def __init__(self,JSON):
        self.id = JSON['id']
        self.buttons = JSON['buttons'] #update this to be an array of button classes
        self.background = JSON['background']

    def update(self, settings):
        #blit
        #updatebuttons
        pass

    def updateButtons(self, settings):
        for button in self.buttons:
            button.draw()
            #if click:
                #button.click()

def scaleMessage(rectSettings, messageRect, messageText):
    messageTextWidth = messageRect.centerx - messageText.get_width() / 2 #Need to change messageRect to an arguement
    messageTextHeight = messageRect.centery - messageText.get_height() / 2
    textSurf = [messageTextWidth, messageTextHeight]
    return textSurf

class Button():
    def __init__(self,JSON):
        self.title = JSON['title']
        self.actionType = JSON['actionType']
        self.actionValue = JSON['actionValue']
        self.center = JSON['center']

    def draw(self,settings):
        buttonRect = pygame.Rect((0,0), (0,0))
        buttonRect.center = self.center
        buttonRect.size = settings.buttonSize
        buttonRectFill = settings.screen.subsurface(buttonRect).convert_alpha()
        buttonRectFill.fill(settings.WHITE)
        pygame.draw.rect(settings.screen, settings.BLACK, buttonRect,1)
        fontDetails = settings.font.render(text, True, settings.BLACK)
        textSurf = scaleMessage(settings, buttonRect, fontDetails)
        settings.screen.blit(buttonRectFill, buttonRect)
        settings.screen.blit(fontDetails, textSurf)

    def click(self,settings):
        if self.actionType == 'nav':
            settings.sceneId = self.actionValue

def drawButton(rectSettings, text, centerParameter): #update center positioning to be based on the other buttons on the screen. Not hardcoded to the button.
    buttonRect = pygame.Rect((0,0), (0,0)) #, rectSettings.buttonSize)
    buttonRect.center = centerParameter
    buttonRect.size = rectSettings.buttonSize

    buttonRectFill = rectSettings.screen.subsurface(buttonRect).convert_alpha()
    buttonRectFill.fill(rectSettings.WHITE)
    pygame.draw.rect(rectSettings.screen, rectSettings.BLACK, buttonRect,1)
    fontDetails = rectSettings.font.render(text, True, rectSettings.BLACK)
    textSurf = scaleMessage(rectSettings, buttonRect, fontDetails)
    rectSettings.screen.blit(buttonRectFill, buttonRect)
    rectSettings.screen.blit(fontDetails, textSurf)

def drawScene(settings):
    sceneDict[settings.sceneId].update()

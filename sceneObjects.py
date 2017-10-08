import pygame

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

    def draw(self, settings, master):
        self.drawBackground(settings)
        self.drawButtons(settings)
        self.drawDayCounter(settings, master)

    def drawBackground(self, settings):
        if self.background == 'NULL':
            settings.screen.blit(settings.screenRectFill,(0,0))
            drawText(settings, self.titleCard, settings.titleRect, color = 'WHITE')
        else:
            settings.screen.blit(self.background,(0,0))

    def drawButtons(self, settings):
        for i, btn in enumerate(self.buttons):
            btn.drawSet(settings, i)

    def drawDayCounter(self, settings, master):
        settings.screen.blit(settings.dayCounterRectFill, settings.dayCounterRect)
        drawText(settings, ("Day: " + str(master.dayCount)), settings.dayCounterRect, color = 'WHITE')

class Button():
    def __init__(self,JSON, settings):
        self.title = JSON['title']
        self.actions = JSON['actions']
        self.rect = pygame.Rect((0,0), (0,0))
        self.rect.size = settings.buttonSize

    def drawSet(self,settings, count):
        #Specify size of button
        btnRect = pygame.Rect(settings.buttonSetPos.topleft, settings.buttonSetPos.size)

        #Specify position of button based on amount already drawn
        btnRect.y = settings.buttonSetPos.y + count*(settings.buttonSize[1] + settings.buttonSetGap)
        self.rect = btnRect

        #Fill the Rect in with WHITE
        buttonRectFill = settings.screen.subsurface(btnRect).convert_alpha()
        buttonRectFill.fill(settings.WHITE)

        #Draw the Black border around the Rect
        pygame.draw.rect(settings.screen, settings.BLACK, btnRect,1)

        #Blit Rect with Black border and White fill
        settings.screen.blit(buttonRectFill, btnRect)

        #Draw button text
        drawText(settings, self.title, self.rect)

    def update(self, master):
        if master.mousePos != None:
            if self.rect.collidepoint(master.mousePos):
                self.click(master)

    def click(self, master):
        for action, actionValue in self.actions.items():
            if action == 'nav':
                master.sceneId = actionValue
            if action == 'day++':
                incrementDay(master, actionValue)

#Dictionary of all scene objects
sceneDict = {}

#Convert JSON into scene objects and fill sceneDict
def unpackScene(JSON, sceneDict):
    for scn in JSON:
        sceneDict[scn['id']]= Scene(scn)

#Dictionary of all button objects
buttonDict = {}

#Convert JSON into button objects and fill buttonDict
def unpackButtons(JSON, buttonDict, settings):
    for butn in JSON:
        buttonDict[butn['title']] = Button(butn, settings)

#Increment Day Counter
def incrementDay(master, numDays):
    master.dayCount += numDays

#Draw text in center of rect
def drawText(settings, text, rect, **kw_parameters):
    textColor = settings.BLACK
    if 'color' in kw_parameters:
        if kw_parameters['color'] == 'WHITE':
            textColor = settings.WHITE
    fontDetails = settings.font.render(text, True, textColor)
    rectTextWidth = rect.centerx - fontDetails.get_width() / 2
    rectTextHeight = rect.centery - fontDetails.get_height() / 2
    textSurf = [rectTextWidth,rectTextHeight]
    settings.screen.blit(fontDetails, textSurf)

import pygame
import random
from teammates import teammateDict

#An object that determines the present background/buttons for the player
class Scene():
    def __init__(self,JSON):
        self.id = JSON['id']
        self.titleCard = JSON['titleCard']
        self.sceneButtons(JSON)
        self.sceneBackground(JSON)
        self.textParagraph = JSON['textData']
        self.advance = JSON['advance']

    def update(self, settings, master):
        if master.rosterPopup:
            if master.mousePos != None:
                master.rosterPopup = False
        else:
            for btn in self.buttons:
                btn.update(master)
            if self.advance:
                if master.mousePos != None:
                    if self.advance['incrementDay']:
                        incrementDay(master, self.advance['incrementDay'])
                    if master.dayCount % 7 == 0:
                        master.sceneId = 's005'
                    else:
                        master.sceneId = self.advance['nav']
            self.rosterButtonUpdate(settings, master)
        master.mousePos = None

    def drawScene(self, settings, master):
        self.drawBackground(settings)
        self.drawButtons(settings)
        if self.id != 's001':
            self.drawDayCounter(settings, master)
            self.drawRosterButton(settings)
        if self.textParagraph:
            drawText(settings.screen, self.textParagraph, settings.WHITE, settings.paragraphRect , settings.font)
        if master.rosterPopup:
            self.drawRosterPopup(settings)
            self.drawRosterTable(settings)

    def drawBackground(self, settings):
        if self.background is None:
            settings.screen.blit(settings.screenRectFill,(0,0))
            if self.titleCard:
                drawTextCenter(settings, self.titleCard, settings.titleRect, color = 'WHITE')
        else:
            settings.screen.blit(self.background,(0,0))

    def drawButtons(self, settings):
        for i, btn in enumerate(self.buttons):
            btn.drawSet(settings, i)

    def drawDayCounter(self, settings, master):
        settings.screen.blit(settings.dayCounterRectFill, settings.dayCounterRect)
        drawTextCenter(settings, ("Day: " + str(master.dayCount)), settings.dayCounterRect, color = 'WHITE')

    def drawRosterButton(self, settings):
        settings.screen.blit(settings.rosterButtonRectFill, settings.rosterButtonRect)
        drawTextCenter(settings, "Roster", settings.rosterButtonRect, color = 'WHITE')

    def drawRosterPopup(self, settings):
        settings.screen.blit(settings.rosterPopupRectFill, settings.rosterPopupRect)
        #Add table of team members here...

    def drawRosterTable(self, settings):
        #settings.screen.blit(settings.rosterPopupTableRectFill, settings.rosterPopupTableRect)
        rowRect = settings.rosterPopupTableRowRect
        #rowSize = settings.rosterPopupTableRect.size
        teammateNames = []
        for k in teammateDict:
            teammateNames.append(k)
        for i in range(settings.rosterPopupTableSetRows()):
            pygame.draw.rect(settings.screen, settings.WHITE, rowRect,1)
            if i < len(teammateNames):
                drawTextCenter(settings, teammateNames[i], rowRect)
            rowRect = pygame.Rect(rowRect.x, rowRect.y + settings.rosterPopupTableRowHeight, rowRect.width, rowRect.height)
        #Create a setting for the height of each row. Then calculate the number of rows.

    def sceneButtons(self, JSON):
        self.buttons = []
        for btn in JSON['buttons']:
            self.buttons.append(buttonDict[btn])

    def sceneBackground(self, JSON):
        if JSON['background']:
            try:
                self.background = pygame.image.load(JSON['background'])
            except:
                self.background = None
        else:
            self.background = None

    def rosterButtonUpdate(self, settings, master):
        if master.mousePos != None:
            if settings.rosterButtonRect.collidepoint(master.mousePos):
                master.rosterPopup = True

class Button():
    def __init__(self,JSON, settings):
        self.id = JSON['id']
        self.title = JSON['title']
        self.actions = JSON['actions']
        #self.rect = pygame.Rect((0,0), (0,0))
        #self.rect.size = settings.buttonSize

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
        drawTextCenter(settings, self.title, self.rect)
        #drawText2(settings.screen, self.title, settings.BLACK, self.rect, settings.font)

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
            if action == 'encounters':
                pickEncounter(master, actionValue)
            if action == 'execute':
                if actionValue == 'matchdaySim':
                    master.sceneDict['s005a'].updateTextData(matchday.matchdaySim(master), 'alert')


#This is the object that holds the buttons across the top.
#Each scene specifies whether to draw it or not.
class TopBar():
    def __init__(self):
        #DayCounter
        self.dayCount = 1
        #ScheduleButton
        #self.scheduleButtonRect = settings.scheduleButtonRect
        #RosterButton
        #self.rosterButtonRect = settings.rosterButtonRect

    def update(self, master):
        '''
        if master.mousePos != None:
            if self.scheduleButtonRect.collidepoint(master.mousePos):
                self.scheduleButtonClick(master)
            elif self.rosterButtonRect.collidepoint(master.mousePos):
                self.rosterButtonClick(master)
        '''
        pass

    def drawTopBar(self, rectSettings):
        self.drawScheduleButton()
        self.drawDayCounter(rectSettings)
        self.drawRosterButton()

    def drawScheduleButton(self):
        pass

    def drawDayCounter(self, rectSettings):
        rectSettings.screen.blit(rectSettings.dayCounterRectFill, rectSettings.dayCounterRect)
        drawTextCenter(rectSettings, ("Day: " + str(self.dayCount)), rectSettings.dayCounterRect, color = 'WHITE')

    def drawRosterButton(self):
        pass

    def scheduleButtonClick(self):
        #Draw Popup surface
        pass

    def rosterButtonClick(self):
        #Draw Popup surface
        pass

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
        buttonDict[butn['id']] = Button(butn, settings)

#Increment Day Counter
def incrementDay(master, numDays):
    master.dayCount += numDays

#Draw text in center of rect
def drawTextCenter(settings, text, rect, **kw_parameters):
    textColor = settings.BLACK
    if 'color' in kw_parameters:
        if kw_parameters['color'] == 'WHITE':
            textColor = settings.WHITE
    fontDetails = settings.font.render(text, True, textColor)
    rectTextWidth = rect.centerx - fontDetails.get_width() / 2
    rectTextHeight = rect.centery - fontDetails.get_height() / 2
    textSurf = [rectTextWidth,rectTextHeight]
    settings.screen.blit(fontDetails, textSurf)

def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            #image = font.render(text[:i], aa, color)
            image = font.render(text[:i], 1, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text

def pickEncounter(master, actionValue):
    pick = random.randrange(len(actionValue))
    master.sceneId = actionValue[pick] #This is dangerous because I shouldn't be updating the master.sceneId in multiple places

import pygame
import random
import matchday
from functions import incrementDay, drawTextCenter, drawText, pickEncounter

#An object that determines the present background/buttons for the player
class Scene():
    def __init__(self, master, JSON):
        self.id = JSON['id']
        self.titleCard = JSON['titleCard']
        self.unpackSceneButtons(master, JSON)
        self.unpackSceneBackground(JSON)
        self.textData = JSON['textData']
        self.actions = JSON['actions']
        self.showTopBar = JSON['showTopBar']

    def update(self, master):
        master.topBar.update(master)
        self.updateSceneButtons(master)
        self.updateActions(master)
        master.mousePos = None

    def updateSceneButtons(self, master):
        for btn in self.buttons:
            btn.update(master)

    def updateTextData(self, text, loc):
        self.textData = {}
        self.textData['text'] = text
        self.textData['loc'] = loc

    def updateActions(self, master):
        if self.actions:
            if master.mousePos != None:
                if self.actions['incrementDay']:
                    incrementDay(master, self.actions['incrementDay'])
                if master.topBar.dayCount % 7 == 0:
                    master.sceneId = 's005'
                else:
                    master.sceneId = self.actions['nav']

    def drawScene(self, settings, master):
        self.drawBackground(settings)
        self.drawButtons(settings)
        if self.showTopBar:
            master.topBar.drawTopBar(settings)
        if self.textData:
            if self.textData['loc'] == 'paragraph':
                drawText(settings.screen, self.textData['text'], settings.WHITE, settings.paragraphRect , settings.font)
            if self.textData['loc'] == 'alert':
                drawText(settings.screen, self.textData['text'], settings.WHITE, settings.alertRect , settings.font)

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

    def unpackSceneButtons(self, master, JSON):
        self.buttons = []
        for btn in JSON['buttons']:
            self.buttons.append(master.buttonDict[btn])

    def unpackSceneBackground(self, JSON):
        if JSON['background']:
            try:
                self.background = pygame.image.load(JSON['background'])
            except:
                self.background = None
        else:
            self.background = None

class Button():
    def __init__(self, JSON):
        self.id = JSON['id']
        self.title = JSON['title']
        self.actions = JSON['actions']

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

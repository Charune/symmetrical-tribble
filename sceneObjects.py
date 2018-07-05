import pygame
import random
import functions
from matchdayCourt import Court

#An object that determines the present background/buttons for the player
class Scene():
    def __init__(self, master, rectSettings, JSON):
        self.id = JSON['id']
        self.unpackSceneButtons(master, JSON)
        self.unpackSceneBackground(JSON)
        self.titleCard = None
        if 'titleCard' in JSON:
            self.titleCard = JSON['titleCard']
        self.showTopBar = True
        if 'showTopBar' in JSON:
            self.showTopBar = JSON['showTopBar']
        self.loadActions = None
        if 'load' in JSON:
            self.loadActions = JSON['load']
        self.textData = None
        if 'textData' in JSON:
            self.textData = JSON['textData']
        self.actions = None
        if 'actions' in JSON:
            self.actions = JSON['actions']
        self.sidebar = None

    def update(self, master, rectSettings, seasonSettings):
        master.topBar.update(master)
        self.updateSceneButtons(master, rectSettings)
        self.updateActions(master, rectSettings, seasonSettings)
        master.mousePos = None

    def updateSceneButtons(self, master, rectSettings):
        for btn in self.buttons:
            btn.update(master, rectSettings)

    def updateTextData(self, text, loc):
        self.textData = {}
        self.textData['text'] = text
        self.textData['loc'] = loc

    def updateActions(self, master, rectSettings, seasonSettings):
        if self.actions:
            if 'execute' in self.actions:
                for e in self.actions['execute']:
                    e(master, rectSettings)
            if master.mousePos != None:
                if 'incrementDay' in self.actions:
                    functions.incrementDay(master, self.actions['incrementDay'])
                if 'nav' in self.actions:
                    if master.dayCount % seasonSettings.matchdayFrequency == 0:
                        self.navScene(master, rectSettings, 's005')
                    else:
                        self.navScene(master, rectSettings, self.actions['nav'])

    def drawScene(self, master, rectSettings):
        self.drawBackground(rectSettings)
        self.drawButtons(master, rectSettings)
        if self.showTopBar:
            master.topBar.drawTopBar(master, rectSettings)
        if self.sidebar:
            self.sidebar.drawSidebar(master, rectSettings)
        if self.textData:
            if self.textData['loc'] == 'paragraph':
                functions.drawText(rectSettings.screen, self.textData['text'], rectSettings.WHITE, rectSettings.paragraphRect , rectSettings.font)
            if self.textData['loc'] == 'alert':
                functions.drawText(rectSettings.screen, self.textData['text'], rectSettings.WHITE, rectSettings.alertRect , rectSettings.font)
        if master.rosterPopup:
            functions.drawRosterPopup(rectSettings)
            functions.drawRosterTable(master, rectSettings)

    def drawBackground(self, settings):
        if self.background is None:
            settings.screen.blit(settings.screenRectFill,(0,0))
            if self.titleCard:
                functions.drawTextCenter(settings, self.titleCard, settings.titleRect, color = 'WHITE')
        else:
            settings.screen.blit(self.background,(0,0))

    def drawButtons(self, master, settings):
        for i, btn in enumerate(self.buttons):
            btn.drawSet(master, settings, i)

    def drawDayCounter(self, settings, master):
        settings.screen.blit(settings.dayCounterRectFill, settings.dayCounterRect)
        functions.drawTextCenter(settings, ("Day: " + str(master.dayCount)), settings.dayCounterRect, color = 'WHITE')

    def navScene(self, master, rectSettings, newSceneId):
        master.sceneId = newSceneId
        master.sceneDict[master.sceneId].loadScene(master, rectSettings)

    def loadScene(self, master, rectSettings):
        if self.loadActions:
            for i in self.loadActions:
                i(master, rectSettings)

    def unpackSceneButtons(self, master, JSON):
        self.buttons = []
        if 'buttons' in JSON:
            for btn in JSON['buttons']:
                self.buttons.append(master.buttonDict[btn])

    def unpackSceneBackground(self, JSON):
        self.background = None
        if 'background' in JSON:
            try:
                self.background = pygame.image.load(JSON['background'])
            except:
                self.background = None


class MatchdayScene(Scene):
    def __init__(self, master, rectSettings, JSON):
        Scene.__init__(self, master, rectSettings, JSON)
        self.courtFocus = 0
        self.courtTeammates = {}
        self.generateCourtRects(master, rectSettings)
        self.matchdayPhase = 0
        #self.loadMatchdayScene(master, rectSettings)

    def loadScene(self, master, rectSettings):
        tempFunctionDict = {'loadMatchdayConfirm':self.loadMatchdayConfirm, 'loadSidebar':self.loadSidebar, 'loadMatchCourts':self.loadMatchCourts}
        if self.loadActions:
            for i in self.loadActions:
                tempFunctionDict[i](master, rectSettings)

    def drawScene(self, master, rectSettings):
        self.drawBackground(rectSettings)
        self.drawMatchCourts(rectSettings)
        self.drawButtons(master, rectSettings)
        self.drawMatchdayButtons(master, rectSettings)
        if self.showTopBar:
            master.topBar.drawTopBar(master, rectSettings)
        if self.sidebar:
            self.sidebar.drawSidebar(master, rectSettings)
        if self.matchdayPhase == 1:
            self.drawMatchOpponent(master, rectSettings)
        if self.textData:
            if self.textData['loc'] == 'paragraph':
                functions.drawText(rectSettings.screen, self.textData['text'], rectSettings.WHITE, rectSettings.paragraphRect , rectSettings.font)
            if self.textData['loc'] == 'alert':
                functions.drawText(rectSettings.screen, self.textData['text'], rectSettings.WHITE, rectSettings.alertRect , rectSettings.font)
        if master.rosterPopup:
            functions.drawRosterPopup(rectSettings)
            functions.drawRosterTable(master, rectSettings)

    def update(self, master, rectSettings, seasonSettings):
        master.topBar.update(master)
        if self.matchdayPhase == 0:
            self.sidebar.updateSidebar(master, rectSettings)
        self.updateMatchCourts(master, rectSettings)
        self.updateSceneButtons(master, rectSettings)
        self.updateMatchdayButtons(master, rectSettings)
        self.updateActions(master, rectSettings, seasonSettings)
        master.mousePos = None

    #NEW
    def drawMatchCourts(self, rectSettings):
        for court in self.courtRects:
            court.draw(rectSettings)
            self.drawMatchVictoryMeter(court.rect, rectSettings)
        self.drawTeammateMatchCourts(rectSettings)
    '''
    def drawMatchCourts(self, rectSettings):
        for c,i in enumerate(self.courtRects):
            if c == self.courtFocus:
                pygame.draw.rect(rectSettings.screen, rectSettings.BLUE, i, 2)
            else:
                pygame.draw.rect(rectSettings.screen, rectSettings.WHITE, i, 1)
            self.drawMatchVictoryMeter(i, rectSettings)
        #self.drawTeammateMatchCourts(rectSettings)
    '''

    #NEW turning off temporarily
    def drawTeammateMatchCourts(self, rectSettings):
        for c, t in self.courtTeammates.items():
            functions.drawTextCenter(rectSettings, t.name, self.courtRects[c].rect, color = 'WHITE')

    def updateMatchCourts(self, master, rectSettings):
        if master.mousePos != None:
            self.clickCourtRect(master, rectSettings)

    '''
    def loadMatchCourts(self, master, settings):
        #master.sceneDict[master.sceneId].variables['courtFocus'] = 0
        self.courtFocus = 0
        self.courtMatchOpponents(master, rectSettings)
    '''
    def addTeammateMatchCourts(self, master, settings, teammate):
        self.courtTeammates[self.courtFocus] = teammate
        self.detectFocus()
        #self.courtTeammates.append(teammate)

    def removeTeammateMatchCourts(self, master, settings, teammate):
        newCourtTeammates = {}
        for k, v in self.courtTeammates.items():
            if v != teammate:
                newCourtTeammates[k] = v
            elif k == self.courtFocus:
                newCourtTeammates[k] = v
            else:
                #self.courtFocus = k
                pass

        self.courtTeammates = newCourtTeammates
        #self.detectFocus()
        #self.courtTeammates = {k:v for k,v in self.courtTeammates.items() if v != teammate}
        #self.courtTeammates.remove(teammate)

    def detectFocus(self):
        for k in range(4):
            if k in self.courtTeammates:
                continue
            else:
                self.courtFocus = k
                break

    def clickCourtRect(self, master, rectSettings):
        for c, r in enumerate(self.courtRects):
            #NEW
            if r.rect.collidepoint(master.mousePos):
            #if r.collidepoint(master.mousePos):
                self.courtFocus = c
                r.isFocus = True
            else: r.isFocus = False

    #NEW
    def generateCourtRects(self, master, rectSettings):
        self.courtRects = []
        for courtOrder in range(4):
            self.courtRects.append(Court(courtOrder, rectSettings))

    '''
    def generateCourtRects(self, master, rectSettings):
        self.courtRects = []
        courtWidth = rectSettings.matchCourtSize[0]
        courtHeight = rectSettings.matchCourtSize[1]
        self.courtRects.append(pygame.Rect((0,0),rectSettings.matchCourtSize))
        self.courtRects.append(pygame.Rect((courtWidth,0),rectSettings.matchCourtSize))
        self.courtRects.append(pygame.Rect((0,courtHeight),rectSettings.matchCourtSize))
        self.courtRects.append(pygame.Rect((courtWidth,courtHeight),rectSettings.matchCourtSize))
    '''
    def courtMatchOpponents(self, master, rectSettings):
        self.opponentList = functions.pickOpponents(master, rectSettings)

    def drawMatchOpponent(self, master, rectSettings):
        for c, o in zip(self.courtRects, self.opponentList):
            #NEW
            oppRect = pygame.Rect(c.rect.left, c.rect.top + 55, c.rect.width, c.rect.height - 55)
            functions.drawTextCenter(rectSettings, str(o.name + ' ' + o.style), oppRect, color = 'BEIGE')

    def matchdayCompete(self, master, rectSettings):
        self.matchWinners = []
        for t, o in zip(self.courtTeammates, self.opponentList):
            self.matchWinners.append(self.matchSim(self.courtTeammates[t],o))
        master.sceneDict['s005a'].updateTextData(self.matchdayResults(self.matchWinners), 'alert')

    def matchdayResults(self, outcome):
        text = ''
        for o in self.matchWinners:
            tempText = '{0} won the the match. It was a {1}. \n'.format(o['victor'],o['type'])
            text = text + tempText
        return text

    def matchSim(self, teammate, opponent):
        skillDif = teammate.skill - opponent.skill
        if skillDif >= 10:
            return {'victor':teammate.name,'type':'blowout'}
        elif skillDif >= 3:
            return {'victor':teammate.name,'type':'dominating win'}
        elif skillDif >= 0:
            return {'victor':teammate.name,'type':'close win'}
        elif skillDif >= -2:
            return {'victor':opponent.name,'type':'close loss'}
        elif skillDif >= -9:
            return {'victor':opponent.name,'type':'bad loss'}
        else:
            return {'victor':opponent.name,'type':'blowout'}

    def drawMatchdayButtons(self, master, rectSettings):
        self.drawMatchdayPlayBtn(master, rectSettings)
        self.drawMatchdayResultsBtn(master, rectSettings)

    def drawMatchdayPlayBtn(self, master, rectSettings):
        if len(self.courtTeammates) >= 4 and self.matchdayPhase == 0:
            self.showMatchdayPlayBtn(master, rectSettings)
            self.matchdayPlayButton.isActive = True
        else:
            self.matchdayPlayButton.isActive = False

    def drawMatchdayResultsBtn(self, master, rectSettings):
        if self.matchdayPhase == 1:
            self.showMatchdayResultsBtn(master, rectSettings)
            self.matchdayResultsButton.isActive = True
        else:
            self.matchdayResultsButton.isActive = False

    def drawMatchEnergyMeters(self, courtRect, rectSettings):
        topMeterRectX = courtRect.x + (courtRect.width - rectSettings.matchVictoryMeterSize[0]) / 2
        topMeterRectY = courtRect.bottom - rectSettings.matchVictoryMeterSize[1] - rectSettings.matchVictoryMeterGap - rectSettings.matchEnergyMeterSize[1]*2
        topMeterRectPos = (topMeterRectX, topMeterRectY)
        topMeterRect = pygame.Rect(topMeterRectPos, rectSettings.matchEnergyMeterSize)
        botMeterRectX = courtRect.x + (courtRect.width - rectSettings.matchVictoryMeterSize[0]) / 2 + (rectSettings.matchVictoryMeterSize[0] - rectSettings.matchEnergyMeterSize[0])
        botMeterRectY = courtRect.bottom - rectSettings.matchVictoryMeterGap - rectSettings.matchEnergyMeterSize[1]
        botMeterRectPos = (botMeterRectX, botMeterRectY)
        botMeterRect = pygame.Rect(botMeterRectPos, rectSettings.matchEnergyMeterSize)

        pygame.draw.rect(rectSettings.screen, rectSettings.WHITE, topMeterRect, 2)
        pygame.draw.rect(rectSettings.screen, rectSettings.WHITE, botMeterRect, 2)
        functions.drawRectFill(topMeterRect, rectSettings.BEIGE, rectSettings)
        functions.drawRectFill(botMeterRect, rectSettings.BEIGE, rectSettings)


    def drawMatchCentralChanceMeter(self, courtRect, rectSettings):
        meterRectX = courtRect.x + (courtRect.width - rectSettings.matchVictoryMeterSize[0]) / 2
        meterRectY = courtRect.bottom - rectSettings.matchVictoryMeterSize[1] - rectSettings.matchVictoryMeterGap - rectSettings.matchEnergyMeterSize[1]
        meterRectPos = (meterRectX, meterRectY)
        meterRect = pygame.Rect(meterRectPos, rectSettings.matchVictoryMeterSize)
        pygame.draw.rect(rectSettings.screen, rectSettings.WHITE, meterRect, 2)

        meterRectPlayerFillRect = pygame.Rect(meterRect.topleft,(meterRect.width/2, meterRect.height))
        meterRectOpponentFillRect =pygame.Rect(meterRectPlayerFillRect.topright,(meterRect.width/2, meterRect.height))
        functions.drawRectFill(meterRectPlayerFillRect, rectSettings.GREEN, rectSettings)
        functions.drawRectFill(meterRectOpponentFillRect, rectSettings.RED, rectSettings)

    def drawMatchVictoryMeter(self, courtRect, rectSettings): #TODO: add the odds of player victory as parameter
        if self.matchdayPhase == 1:
            self.drawMatchCentralChanceMeter(courtRect, rectSettings)
            self.drawMatchEnergyMeters(courtRect, rectSettings)
        else:
            pass

    def loadMatchdayConfirm(self, master, rectSettings):
        btnMatchdayPlay = {'id':'btnGamedayPlay'
            ,'title':'Play'
            ,'actions':{'execute':[self.clickMatchdayPlay]}}#[functions.matchdayCont]}} #TODO:Move funcions. function to self
        btnMatchdayResults = {'id':'btnGamedayResults'
            ,'title':'Results'
            ,'actions':{'execute':[self.clickMatchdayResults],'nav':'s005a'}}
        centerButtonRect = pygame.Rect((rectSettings.screenRect.centerx - 180, rectSettings.screenRect.centery - 20), (rectSettings.buttonSetPos.size))
        self.matchdayPlayButton = Button(btnMatchdayPlay, self)
        self.matchdayPlayButton.rect = centerButtonRect
        self.matchdayPlayButton.isActive = False
        self.matchdayResultsButton = Button(btnMatchdayResults, self)
        self.matchdayResultsButton.rect = centerButtonRect
        self.matchdayResultsButton.isActive = False

    def loadSidebar(self, master, rectSettings):
        master.sceneDict[master.sceneId].sidebar = Sidebar(master, rectSettings)

    def loadMatchCourts(self, master, rectSettings):
        master.sceneDict[master.sceneId].courtFocus = 0
        master.sceneDict[master.sceneId].matchdayPhase = 0
        master.sceneDict[master.sceneId].courtMatchOpponents(master, rectSettings)

    def showMatchdayPlayBtn(self, master, rectSettings):
        self.matchdayPlayButton.drawButton(master, rectSettings)


    def showMatchdayResultsBtn(self, master, rectSettings):
        self.matchdayResultsButton.drawButton(master, rectSettings)

    def clickMatchdayResults(self, master, rectSettings):
        self.matchdayCompete(master, rectSettings)

    def clickMatchdayPlay(self, master, rectSettings):
        self.matchdayPhase = 1

    def updateMatchdayButtons(self, master, rectSettings):
        self.matchdayPlayButton.update(master, rectSettings)
        self.matchdayResultsButton.update(master, rectSettings)

class Button():
    def __init__(self, JSON, parentScene = None):
        self.id = JSON['id']
        self.title = JSON['title']
        self.actions = JSON['actions']
        self.isActive = True
        self.__parent__ = parentScene

    def drawSet(self, master, settings, count):
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
        functions.drawTextCenter(settings, self.title, self.rect)
        #drawText2(settings.screen, self.title, settings.BLACK, self.rect, settings.font)
        self.setButtonScene(master.sceneDict[master.sceneId])

    def update(self, master, rectSettings):
        if master.mousePos != None:
            if self.rect.collidepoint(master.mousePos) and self.isActive:
                self.click(master, rectSettings)

    def click(self, master, rectSettings):
        for action, actionValue in self.actions.items():
            if action == 'day++':
                functions.incrementDay(master, actionValue)
            if action == 'encounters':
                functions.pickEncounter(master, actionValue)
            if action == 'execute':
                for e in actionValue:
                    e(master, rectSettings)
            if action == 'nav':
                #master.sceneId = actionValue
                self.__parent__.navScene(master, rectSettings, actionValue)
                '''
                if actionValue == 'matchdaySim':
                    master.sceneDict['s005a'].updateTextData(matchday.matchdaySim(master), 'alert')
                if actionValue == 'matchdayCont':
                    master.sceneDict[master.sceneId].matchdayContinue = True
                '''
    def drawButton(self, master, rectSetting):
        #Fill the Rect in with WHITE
        buttonRectFill = rectSetting.screen.subsurface(self.rect).convert_alpha()
        buttonRectFill.fill(rectSetting.WHITE)
        #Draw the Black border around the Rect
        pygame.draw.rect(rectSetting.screen, rectSetting.BLACK, self.rect,1)
        #Blit Rect with Black border and White fill
        rectSetting.screen.blit(buttonRectFill, self.rect)
        #Draw button text
        functions.drawTextCenter(rectSetting, self.title, self.rect)
        #self.setButtonScene(master.sceneDict[master.sceneId])

    def setButtonScene(self, parentScene):
        self.__parent__ = parentScene

#This is the object that holds the buttons across the top.
#Each scene specifies whether to draw it or not.
class TopBar():
    def __init__(self, rectSettings):
        #ScheduleButton
        #self.scheduleButtonRect = settings.scheduleButtonRect
        #RosterButton
        self.rosterButtonRect = rectSettings.rosterButtonRect

    def update(self, master):
        if master.mousePos != None:
            if master.rosterPopup:
                master.rosterPopup = False
            elif self.rosterButtonRect.collidepoint(master.mousePos):
                master.rosterPopup = True
        '''
        elif master.mousePos != None:
            if self.scheduleButtonRect.collidepoint(master.mousePos):
                self.scheduleButtonClick(master)
            elif self.rosterButtonRect.collidepoint(master.mousePos):
                self.rosterButtonClick(master)
        '''

    def drawTopBar(self, master, rectSettings):
        self.drawScheduleButton()
        self.drawDayCounter(master, rectSettings)
        self.drawRosterButton(rectSettings)

    def drawScheduleButton(self):
        pass

    def drawDayCounter(self, master, rectSettings):
        rectSettings.screen.blit(rectSettings.dayCounterRectFill, rectSettings.dayCounterRect)
        functions.drawTextCenter(rectSettings, ("Day: " + str(master.dayCount)), rectSettings.dayCounterRect, color = 'WHITE')

    def drawRosterButton(self, rectSettings):
        rectSettings.screen.blit(rectSettings.rosterButtonRectFill, rectSettings.rosterButtonRect)
        functions.drawTextCenter(rectSettings, "Roster", rectSettings.rosterButtonRect, color = 'WHITE')

    def scheduleButtonClick(self):
        #Draw Popup surface
        pass

    def rosterButtonClick(self):
        #Draw Popup surface
        pass

class Sidebar():
    def __init__(self, master, rectSettings):
        self.generateTeammateList(master, rectSettings)
        #self.teammateList = master.playerTeam.teammates
        #self.teammateRects = self.generateTeammateRects(master, rectSettings)

    def generateTeammateList(self, master, rectSettings):
        self.teammateList = []
        teammateRect = pygame.Rect((rectSettings.sidebarRect.topleft), (rectSettings.sidebarRect.width, rectSettings.sidebarRosterRowHeight))
        for k in master.playerTeam.teammates: # self.teammateList:
            teammateCell = {}
            teammateCell['rect'] = teammateRect
            teammateCell['details'] = k
            teammateCell['clicked'] = False
            self.teammateList.append(teammateCell)
            teammateRect = pygame.Rect(teammateRect.x, teammateRect.y + rectSettings.sidebarRosterRowHeight, teammateRect.width, teammateRect.height)
        self.clickedSidebarRoster(master, rectSettings)

    def drawSidebar(self, master, rectSettings):
        pygame.draw.rect(rectSettings.screen, rectSettings.WHITE, rectSettings.sidebarRect, 1)
        self.drawSidebarRoster(master, rectSettings)

    '''
    def drawSidebarRoster(self, master, settings):
        rowRect = pygame.Rect((settings.sidebarRect.topleft), (settings.sidebarRect.width, settings.sidebarRosterRowHeight))
        for k in self.teammateList:
            pygame.draw.rect(settings.screen, settings.WHITE, rowRect, 3)
            functions.drawTextCenter(settings, k.name, rowRect, color = 'WHITE')
            rowRect = pygame.Rect(rowRect.x, rowRect.y + settings.sidebarRosterRowHeight, rowRect.width, rowRect.height)
    '''
    def drawSidebarRoster(self, master, rectSettings):
        for t in self.teammateList:
            if t['clicked']:
                pygame.draw.rect(rectSettings.screen, rectSettings.WHITE, t['rect'], 1)
                functions.drawTextCenter(rectSettings, t['details'].name + ' ' + t['details'].style, t['rect'], color = 'RED')
            else:
                pygame.draw.rect(rectSettings.screen, rectSettings.WHITE, t['rect'], 2)
                functions.drawTextCenter(rectSettings, t['details'].name + ' ' + t['details'].style, t['rect'], color = 'WHITE')

    def updateSidebar(self, master, rectSettings):
        self.updateSidebarRoster(master, rectSettings)
        if master.mousePos != None:
            #Remove teammates that are clicked.
            self.sidebarClick(master, rectSettings)

    def updateSidebarRoster(self, master, rectSettings):
        self.clickedSidebarRoster(master, rectSettings)

    def clickedSidebarRoster(self, master, rectSettings):
        for t in self.teammateList:
            for k,v in master.sceneDict[master.sceneId].courtTeammates.items():
                if t['details'] == v:
                    t['clicked'] = True
                    break
                else:
                    t['clicked'] = False

    def sidebarClick(self, master, rectSettings):
        for t in self.teammateList:
            if t['rect'].collidepoint(master.mousePos):
                if t['clicked']:
                    master.sceneDict[master.sceneId].removeTeammateMatchCourts(master, rectSettings, t['details'])
                    master.sceneDict[master.sceneId].addTeammateMatchCourts(master, rectSettings, t['details'])
                else:
                    #t['clicked'] = True
                    master.sceneDict[master.sceneId].addTeammateMatchCourts(master, rectSettings, t['details'])

        '''
        for t in self.teammateList:
            if t['rect'].collidepoint(master.mousePos):
                addTeammateMatchCourts(master, rectSettings, t)
        self.teammateList[:] = [t for t in self.teammateList if not t['rect'].collidepoint(master.mousePos)]
        '''
    '''
    def generateTeammateRects(self, master, rectSettings):
        teammateRects = []
        teammateRect = pygame.Rect((rectSettings.sidebarRect.topleft), (rectSettings.sidebarRect.width, rectSettings.sidebarRosterRowHeight))
        for k in self.teammateList:
            teammateRects.append(teammateRect)
            teammateRect = pygame.Rect(teammateRect.x, teammateRect.y + rectSettings.sidebarRosterRowHeight, teammateRect.width, teammateRect.height)
        return teammateRects
    '''
'''
class Popup():
    def __init__(self, RectSettings):
        pass
    def drawRosterPopup(self, settings):
        settings.screen.blit(settings.rosterPopupRectFill, settings.rosterPopupRect)
'''

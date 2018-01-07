import pygame
import random
import matchday
import functions

#An object that determines the present background/buttons for the player
class Scene(): #TODO: Make a subclass of Scene for matchdayCourts scene
    def __init__(self, master, rectSettings, JSON):
        self.id = JSON['id']
        self.titleCard = JSON['titleCard']
        self.unpackSceneButtons(master, JSON)
        self.unpackSceneBackground(JSON)
        self.textData = JSON['textData']
        self.actions = JSON['actions']
        self.showTopBar = JSON['showTopBar']
        if 'load' in JSON:
            self.loadActions = JSON['load']
        else:
            self.loadActions = None
        self.sidebar = None
        self.variables = {}

    def update(self, master, rectSettings):
        master.topBar.update(master)
        '''
        if self.sidebar:
            self.sidebar.updateSidebar(master, rectSettings)
        '''
        self.updateSceneButtons(master, rectSettings)
        self.updateActions(master, rectSettings)
        master.mousePos = None

    def updateSceneButtons(self, master, rectSettings):
        for btn in self.buttons:
            btn.update(master, rectSettings)

    def updateTextData(self, text, loc):
        self.textData = {}
        self.textData['text'] = text
        self.textData['loc'] = loc

    def updateActions(self, master, rectSettings):
        if self.actions:
            if 'execute' in self.actions:
                for e in self.actions['execute']:
                    e(master, rectSettings)
                #self.actions['execute'](master,rectSettings)
            if master.mousePos != None:
                if 'incrementDay' in self.actions:
                    functions.incrementDay(master, self.actions['incrementDay'])
                if 'nav' in self.actions:
                    if master.dayCount % 2 == 0:
                        #master.sceneId = 's005'
                        functions.navScene(master, rectSettings, 's005')
                    else:
                        #master.sceneId = self.actions['nav']
                        functions.navScene(master, rectSettings, self.actions['nav'])

    def drawScene(self, rectSettings, master):
        self.drawBackground(rectSettings)
        self.drawButtons(rectSettings)
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

    def drawButtons(self, settings):
        for i, btn in enumerate(self.buttons):
            btn.drawSet(settings, i)

    def drawDayCounter(self, settings, master):
        settings.screen.blit(settings.dayCounterRectFill, settings.dayCounterRect)
        functions.drawTextCenter(settings, ("Day: " + str(master.dayCount)), settings.dayCounterRect, color = 'WHITE')

    def loadScene(self, master, rectSettings):
        if self.loadActions:
            for i in self.loadActions:
                #self.sidebar = i(master, rectSettings)
                i(master, rectSettings)

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

class MatchdayScene(Scene):
    def __init__(self, master, rectSettings, JSON):
        Scene.__init__(self, master, rectSettings, JSON)
        self.courtFocus = 0
        self.courtTeammates = {}
        self.generateCourtRects(master, rectSettings)
        self.matchdayContinue = False

    def drawScene(self, rectSettings, master):
        self.drawBackground(rectSettings)
        self.drawMatchCourts(rectSettings)
        self.drawButtons(rectSettings)
        if self.showTopBar:
            master.topBar.drawTopBar(master, rectSettings)
        if self.sidebar:
            self.sidebar.drawSidebar(master, rectSettings)
        if self.matchdayContinue:
            self.drawMatchOpponent(master, rectSettings)
        if self.textData:
            if self.textData['loc'] == 'paragraph':
                functions.drawText(rectSettings.screen, self.textData['text'], rectSettings.WHITE, rectSettings.paragraphRect , rectSettings.font)
            if self.textData['loc'] == 'alert':
                functions.drawText(rectSettings.screen, self.textData['text'], rectSettings.WHITE, rectSettings.alertRect , rectSettings.font)
        if master.rosterPopup:
            functions.drawRosterPopup(rectSettings)
            functions.drawRosterTable(master, rectSettings)

    def update(self, master, rectSettings):
        master.topBar.update(master)
        self.sidebar.updateSidebar(master, rectSettings)
        self.updateMatchCourts(master, rectSettings)
        self.updateSceneButtons(master, rectSettings)
        self.updateActions(master, rectSettings)
        master.mousePos = None

    def drawMatchCourts(self, rectSettings):
        for c,i in enumerate(self.courtRects):
            if c == self.courtFocus:
                pygame.draw.rect(rectSettings.screen, rectSettings.BLUE, i, 2)
            else:
                pygame.draw.rect(rectSettings.screen, rectSettings.WHITE, i, 1)
        self.drawTeammateMatchCourts(rectSettings)

    def drawTeammateMatchCourts(self, rectSettings):
        for c, t in self.courtTeammates.items():
            functions.drawTextCenter(rectSettings, t.name, self.courtRects[c], color = 'WHITE')

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
            if r.collidepoint(master.mousePos):
                self.courtFocus = c

    def generateCourtRects(self, master, rectSettings):
        self.courtRects = []
        courtWidth = (rectSettings.screenRect.width - 224) / 2
        courtHeight = rectSettings.screenRect.height/2
        self.courtRects.append(pygame.Rect((0,0),(courtWidth,courtHeight)))
        self.courtRects.append(pygame.Rect((courtWidth,0),(courtWidth,courtHeight)))
        self.courtRects.append(pygame.Rect((0,courtHeight),(courtWidth,courtHeight)))
        self.courtRects.append(pygame.Rect((courtWidth,courtHeight),(courtWidth,courtHeight)))

    def courtMatchOpponents(self, master, rectSettings):
        self.opponentList = functions.pickOpponents(master, rectSettings)

    def drawMatchOpponent(self, master, rectSettings):
        for c, o in zip(self.courtRects, self.opponentList):
            oppRect = pygame.Rect(c.left, c.top + 55, c.width, c.height - 55)
            functions.drawTextCenter(rectSettings, str(o.name + ' ' + o.style), oppRect, color = 'BEIGE')

    def matchdayCompete(self, master, rectSettings):
        print('working')
        self.matchWinners = []
        print(len(self.courtTeammates))
        print(len(self.opponentList))
        for t, o in zip(self.courtTeammates, self.opponentList):
            self.matchWinners.append(self.matchSim(self.courtTeammates[t],o))
        master.sceneDict['s005a'].updateTextData(self.matchdayResults(self.matchWinners), 'alert')

    def simMatch(self, teammate, opponent):
        return opponent.name

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

    def matchdaySim(self, master):
        opponents = matchdayOpponent(master.opponentsDict)[:]
        outcome = []
        for tm in master.playerTeam.teammates:
            pick = random.randrange(len(opponents))
            outcome.append(matchSim(tm,opponents[pick]))
            del opponents[pick]
        return matchdayResults(outcome)

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
        functions.drawTextCenter(settings, self.title, self.rect)
        #drawText2(settings.screen, self.title, settings.BLACK, self.rect, settings.font)

    def update(self, master, rectSettings):
        if master.mousePos != None:
            if self.rect.collidepoint(master.mousePos):
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
                functions.navScene(master, rectSettings, actionValue)
                '''
                if actionValue == 'matchdaySim':
                    master.sceneDict['s005a'].updateTextData(matchday.matchdaySim(master), 'alert')
                if actionValue == 'matchdayCont':
                    master.sceneDict[master.sceneId].matchdayContinue = True
                '''


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

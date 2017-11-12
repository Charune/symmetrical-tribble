import pygame
from teams import Team
from sceneObjects import Scene, Button, TopBar
import json

class RectSettings():
    def __init__(self):
        #Color Codes
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.BLUE = (0,0,255)
        self.GREEN = (0,255,0)
        self.RED = (255,0,0)
        self.BEIGE = (205,183,158)
        #self.BEIGE = (205,175,149)

        #Screen details
        self.size = (1024,768)
        self.screenRect = pygame.Rect((0,0), self.size)
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill(self.BLACK)
        self.screenRectFill = self.screen.subsurface(self.screenRect).convert_alpha()

        #Font details
        self.font = pygame.font.SysFont('Calibri',22,True,False)
        self.titleRect = pygame.Rect((0,0), (self.size[0], self.size[1]/8))

        #Button details
        self.buttonSize = (145,40)
        self.buttonSetPos = self.buttonSetPos()
        self.buttonSetGap = 60

        #Paragraph Box details
        self.paragraphRect = pygame.Rect(70,600,800,200)

        #Alert Box details
        self.alertRect = pygame.Rect(350,300,600,150)

        #DayCounter details
        self.dayCounterRect = pygame.Rect(940,0,72,28)
        self.dayCounterRectFill = self.screen.subsurface(self.dayCounterRect).convert_alpha()
        self.dayCounterRectFill.fill(self.BEIGE)

    #Define the structure of a set of buttons
    def buttonSetPos(self):
        x = self.screenRect.width/2 - self.buttonSize[0]/2
        y = self.screenRect.height/4
        return pygame.Rect((x,y),self.buttonSize)

class SeasonSettings():
    def __init__(self):
        self.matchdaysPerSeason = 20

class Master():
    def __init__(self, settings):
        #Initial Scene
        self.sceneId = 's001'
        self.mousePos = None
        #Unpack master objects
        self.unpackPlayerSchool(json.playerTeamJSON)
        self.unpackOpponents(json.opponentList)
        self.unpackButtons(json.buttonList)
        self.unpackScenes(json.sceneList)
        self.staffList = []
        self.studentBody = None
        self.topBar = TopBar()

    def unpackPlayerSchool(self, playerTeam):
        self.playerTeam = Team(playerTeam)

    def unpackOpponents(self, opponentTeams):
        opponentDict = {}
        for opponentTeam in opponentTeams:
            opponentDict[opponentTeam['id']] = Team(opponentTeam)
        self.opponentDict = opponentDict

    def unpackScenes(self, scenes):
        sceneDict = {}
        for scn in scenes:
            sceneDict[scn['id']]= Scene(self, scn)
        self.sceneDict = sceneDict

    def unpackButtons(self, buttons):
        buttonDict = {}
        for butn in buttons:
            buttonDict[butn['id']] = Button(butn)
        self.buttonDict = buttonDict

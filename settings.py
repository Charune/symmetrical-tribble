import pygame

class RectSettings():
    def __init__(self):
        #Color Codes
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.BLUE = (0,0,255)
        self.GREEN = (0,255,0)
        self.RED = (255,0,0)
        #self.BEIGE = (205,175,149)
        self.BEIGE = (205,183,158)

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

        #Advance details
        self.advanceSize = self.screenRect


        #Dialog Box details
        self.messageRect = pygame.Rect(250,300,500,200)
        self.messageRectFill = self.screen.subsurface(self.messageRect).convert_alpha()
        self.messageRectFill.fill(self.BLACK)

        #Paragraph Box details
        self.paragraphRect = pygame.Rect(70,600,800,200)

        #DayCounter details
        self.dayCounterRect = pygame.Rect(940,0,72,28)
        self.dayCounterRectFill = self.screen.subsurface(self.dayCounterRect).convert_alpha()
        self.dayCounterRectFill.fill(self.BEIGE)

    #Define the structure of a set of buttons
    def buttonSetPos(self):
        x = self.screenRect.width/2 - self.buttonSize[0]/2
        y = self.screenRect.height/4
        return pygame.Rect((x,y),self.buttonSize)

class Master():
    def __init__(self):
        #Initial Scene
        self.sceneId = 's001'
        self.mousePos = None
        self.dayCount = 1

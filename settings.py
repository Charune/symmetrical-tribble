import pygame

pygame.init()

class RectSettings():
    def __init__(self):
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.BLUE = (0,0,255)
        self.GREEN = (0,255,0)
        self.RED = (255,0,0)
        self.size = (1024,768)
        self.screenRect = pygame.Rect((0,0), self.size)
        self.screen = pygame.display.set_mode(self.size)
        self.screenRectFill = self.screen.subsurface(self.screenRect).convert_alpha()
        self.font = pygame.font.SysFont('Calibri',22,True,False)

        self.buttonSize = (145,40)
        self.buttonSetPos = self.buttonSetPos()
        self.buttonSetGap = 60
        self.messageRect = pygame.Rect(250,300,500,200)
        self.messageRectFill = self.screen.subsurface(self.messageRect).convert_alpha()
        self.messageRectFill.fill(self.BLACK)

    def buttonSetPos(self):
        x = self.screenRect.width/2 - self.buttonSize[0]/2
        y = self.screenRect.height/4
        return pygame.Rect((x,y),self.buttonSize)
        #return pygame.Rect((436,192),(145,40))

class Master():
    def __init__(self):
        self.sceneId = 's001'
        self.mousePos = None

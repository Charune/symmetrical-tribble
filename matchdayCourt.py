import pygame

#This class represents everything in a single court during matchday.
class Court():
    def __init__(self, courtOrder, rectSettings):
        self.order = courtOrder # 1-4
        #self.matchMeter = matchMeter()
        self.isFocus = False
        self.size = rectSettings.matchCourtSize # (width, height)
        self.genCourtRect()
        self.teammate = None
        self.opponent = None
        self.rectSettings = rectSettings.screen

    def genCourtRect(self):
        courtWidth = self.size[0]
        courtHeight = self.size[1]
        widthMtplr = (self.order) % 2 # 1,0,1,0
        heightMtplr = int((self.order)/2) # 0,0,1,1
        self.rect = pygame.Rect((widthMtplr*courtWidth, heightMtplr*courtHeight), self.size)

    def draw(self, rectSettings):
        if self.isFocus:
            pygame.draw.rect(rectSettings.screen, rectSettings.BLUE, self.rect, 2)
        else:
            pygame.draw.rect(rectSettings.screen, rectSettings.WHITE, self.rect, 1)

    #Old style before Court class.
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

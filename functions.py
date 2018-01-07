import random
import pygame
import sceneObjects

#Increment Day Counter
def incrementDay(master, numDays):
    master.dayCount += numDays

#Draw text in center of rect
def drawTextCenter(settings, text, rect, **kw_parameters):
    textColor = settings.BLACK
    if 'color' in kw_parameters:
        if kw_parameters['color'] == 'WHITE':
            textColor = settings.WHITE
        elif kw_parameters['color'] == 'RED':
            textColor = settings.RED
        elif kw_parameters['color'] == 'BEIGE':
            textColor = settings.BEIGE
    fontDetails = settings.font.render(text, True, textColor)
    rectTextWidth = rect.centerx - fontDetails.get_width() / 2
    rectTextHeight = rect.centery - fontDetails.get_height() / 2
    textSurf = [rectTextWidth,rectTextHeight]
    settings.screen.blit(fontDetails, textSurf)

def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    y = rect.top
    lineSpacing = -2
    # get the height of the font
    fontHeight = font.size("Tg")[1]
    while text:
        i = 1
        newline = False
        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break
        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text) and newline is False:
            if text[i] == '\n':
                newline = True
                break
            i += 1
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
        if newline:
            text = text[i+1:]
        else:
            text = text[i:]
    return text

def pickEncounter(master, actionValue):
    pick = random.randrange(len(actionValue))
    master.sceneId = actionValue[pick] #This is dangerous because I shouldn't be updating the master.sceneId in multiple places

def drawRosterPopup(settings):
    settings.screen.blit(settings.rosterPopupRectFill, settings.rosterPopupRect)

def drawRosterTable(master, settings):
    #settings.screen.blit(settings.rosterPopupTableRectFill, settings.rosterPopupTableRect)
    rowRect = settings.rosterPopupTableRowRect
    #rowSize = settings.rosterPopupTableRect.size
    teammateNames = []
    for k in master.playerTeam.teammates:
        teammateNames.append(k.name)
    for i in range(settings.rosterPopupTableSetRows()):
        pygame.draw.rect(settings.screen, settings.BLACK, rowRect,1)
        if i < len(teammateNames):
            drawTextCenter(settings, teammateNames[i], rowRect)
        rowRect = pygame.Rect(rowRect.x, rowRect.y + settings.rosterPopupTableRowHeight, rowRect.width, rowRect.height)
    #Create a setting for the height of each row. Then calculate the number of rows.

def loadSidebar(master, rectSettings):
    master.sceneDict[master.sceneId].sidebar = sceneObjects.Sidebar(master, rectSettings)

def loadMatchCourts(master, rectSettings):
    #master.sceneDict[master.sceneId].variables['courtFocus'] = 0
    master.sceneDict[master.sceneId].courtFocus = 0
    master.sceneDict[master.sceneId].matchdayPhase = 0
    master.sceneDict[master.sceneId].courtMatchOpponents(master, rectSettings)

def pickOpponents(master, rectSettings):
    opponentList = []
    opponents = master.opponentsDict['schl001'].teammates[:]
    for i in range(4):
        pick = random.randrange(len(opponents))
        opponentList.append(opponents[pick])
        del opponents[pick]
    return opponentList

def navScene(master, rectSettings, newSceneId):
    master.sceneId = newSceneId
    master.sceneDict[master.sceneId].loadScene(master, rectSettings)

def matchdayCont(master, rectSettings):
    master.sceneDict[master.sceneId].matchdayContinue = True

def matchdaySim(master, rectSettings):
    #master.sceneDict['s005a'].updateTextData(master.sceneDict['s005a'].matchdaySim(master), 'alert')
    pass

def matchdayComp(master, rectSettings):
    master.sceneDict[master.sceneId].matchdayCompete(master, rectSettings)

def testFunc():
    print('hello')

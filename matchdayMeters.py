
#This class operates the meters during matchday.
class matchMeter():
    def __init__(self, courtRect, courtNum):
        self.courtNum = courtNum # 1-4
        self.courtRect = courtRect

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

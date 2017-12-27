teammateNamesArray = { 'name':['Nami','Josey','Sansa','Summer']
}

tm1 = {'name':'Nami'}
tm2 = {'name':'Josey'}
tm3 = {'name':'Sansa'}
tm4 = {'name':'Summer'}

teammatesJSON = [tm1, tm2, tm3, tm4]

class Teammate():
    def __init__(self, JSON):
        self.name = JSON['name'] #JSON['name']
        self.energy = 1
        self.heart = 3 #0-6
        self.skill = 1

teammateDict = {}
def unpackTeammates(JSON, teammateDict):
    for teammate in JSON:
        teammateDict[teammate['name']] = Teammate(teammate)
'''
def unpackTeammates(JSON, teammateDict):
    for teammate in JSON['name']:
        teammateDict[teammate] = Teammate(teammate)


def generateTeammatesJSON(names):
    teammateDict = {}
    for name in names:
        teammateDict[name] =
'''

def listTeammates():
    pass

def drawRosterTeammates():
    pass

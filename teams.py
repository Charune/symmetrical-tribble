class Teammate():
    def __init__(self, dict):
        self.id = dict['id']
        self.name = dict['name']
        self.skill = dict['skill']
        self.year = dict['year']
        self.grades = dict['grades']

class Team():
    def __init__(self, JSON):
        self.id = JSON['id']
        self.name = JSON['name']
        self.teammates = []
        if JSON['teammates']:
            self.generateJSONTeammates(JSON['teammates'])
        else:
            self.generateRandomTeammates()

    def generateJSONTeammates(self, tmList):
        for tm in tmList:
            self.teammates.append(Teammate(tm))

    def generateRandomTeammates(self):
        for i in range(4):
            self.teammates.append(self.generateRandTeammate(i))

    def generateRandTeammate(self, count):
        randomDict = {'id': 'opp00{0}_{1}'.format(count+1,self.id)
            ,'name':'Yuna{0}'.format(count)
            ,'year':2015
            ,'grades':75
            ,'skill':2
            }
        return Teammate(randomDict)

    def showTeammates(self):
        print('School Name: ' + self.name)
        print('Number of Students: ' + str(len(self.teammates)))
        for c,o in enumerate(self.teammates):
            print('Student ' + str(c) + ' Name: ' + o.name)
            print('Year: ' + str(o.year))
            print('grades: ' + str(o.grades))
            print('skill: ' + str(o.skill))

#object that holds all students, those on the team and those at the school.
class StudentBody():
    pass

#Every staff npc (dean, coaches, hacker)
class Staff():
    pass

staffList = []

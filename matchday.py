import random

def matchdaySim(master):
    opponents = matchdayOpponent(master.opponentDict)[:]
    outcome = []
    for tm in master.playerTeam.teammates:
        pick = random.randrange(len(opponents))
        outcome.append(matchSim(tm,opponents[pick]))
        del opponents[pick]
    return matchdayResults(outcome)

#Determine which opponents the player's team will be facing.
def matchdayOpponent(opponentsDict):
    return opponentsDict['schl001'].teammates

def matchSim(teammate, opponent):
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

def matchdayResults(outcome):
    text = ''
    for o in outcome:
        tempText = '{0} won the the match. It was a {1}. \n'.format(o['victor'],o['type'])
        text = text + tempText
    return text

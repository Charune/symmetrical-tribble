import functions
#Encounters list
TennisCourtTrainEncounters = ['s003a','s003b']

#Button JSONs
btnStart = {'id':'btnStart'
    ,'title':'Start'
    ,'actions':{'nav':'s002'}}
btnBack = {'id':'btnBack'
    ,'title':'Back'
    ,'actions':{'nav':'s002'}}
btnTennisCourt = {'id':'btnTennisCourt'
    ,'title':'Tennis Courts'
    ,'actions':{'nav':'s003'}}
btnTennisCourtTrain = {'id':'btnTennisCourtTrain'
    ,'title':'Train'
    ,'actions':{'encounters':TennisCourtTrainEncounters}}
btnGym = {'id':'btnGym'
    ,'title':'Gym'
    ,'actions':{'nav':'s004'}}
btnGameday = {'id':'btnGameday'
    ,'title':'Game Day'
    ,'actions':{'execute':'matchdaySim','nav':'s005b'}}
btnGamedayConf = {'id':'btnGamedayConf'
    ,'title':'Confirm'
    ,'actions':{'nav':'s005a'}}
buttonList = [btnStart,btnBack,btnTennisCourt,btnTennisCourtTrain,btnGym,btnGameday,btnGamedayConf]

#Scene JSONs
startSceneJSON = {'id':'s001'
    ,'buttons':['btnStart']
    ,'background':None
    ,'showTopBar':False
    ,'titleCard':'Start'
    ,'actions':None
    ,'textData':None}
mainSceneJSON = {'id':'s002'
    ,'buttons':['btnGym','btnTennisCourt']
    ,'background':None
    ,'showTopBar':True
    ,'titleCard':'Main'
    ,'actions':None
    ,'textData':None}
gymSceneJSON = {'id':'s004'
    ,'buttons':['btnBack']
    ,'background':None
    ,'showTopBar':True
    ,'titleCard':'Gymnasium'
    ,'actions':None
    ,'textData':None}
tennisCourtsSceneJSON = {'id':'s003'
    ,'buttons':['btnTennisCourtTrain','btnBack']
    ,'background':r'Art\SoftTennis3Scaled.png'
    ,'showTopBar':True
    ,'titleCard':'Tennis Courts'
    ,'actions':None
    ,'textData':None}
#Idea for improvements to encounters. Have a single encounter scene.
#But modify the text and actions based on the rolls?
tennisCourtsEncounterTrainJSON = {'id':'s003a'
    ,'buttons':[]
    ,'background':None
    ,'showTopBar':False
    ,'titleCard':None
    ,'actions':{'nav':'s002','incrementDay':1}
    ,'textData':{'loc':'paragraph','text':"A few hours pass as you run the team through a series of drills. By the end everyone is exhausted."}}
tennisCourtsEncounterInjuryJSON = {'id':'s003b'
    ,'buttons':[]
    ,'background':None
    ,'showTopBar':False
    ,'titleCard':None
    ,'actions':{'nav':'s002','incrementDay':1}
    ,'textData':{'loc':'paragraph','text':"You focus on improving your players' agility. Unfortunately one player takes a spill and sprains an ankle."}}
#TODO: Once player database is implemented, update text to take a random player's name.
gamedaySceneJSON = {'id':'s005'
    ,'buttons':['btnGameday']
    ,'background':None
    ,'showTopBar':True
    ,'titleCard':'Game Day'
    ,'actions':None
    ,'textData':None}
gamedayResultsJSON = {'id':'s005a'
    ,'buttons':[]
    ,'background':None
    ,'showTopBar':False
    ,'titleCard':None
    ,'actions':{'nav':'s002','incrementDay':1}
    ,'textData':None}
gamedayCourtsJSON = {'id':'s005b'
    ,'buttons':['btnGamedayConf']
    ,'background':None
    ,'showTopBar':False
    ,'titleCard':None
    #,'actions':{'execute': [functions.drawMatchCourts]}
    ,'actions':None
    ,'load':[functions.loadSidebar]
    ,'textData':None
    ,'sceneType':'MatchdayScene'}

sceneList = [startSceneJSON,mainSceneJSON ,gymSceneJSON ,tennisCourtsSceneJSON
    ,tennisCourtsEncounterTrainJSON ,tennisCourtsEncounterInjuryJSON
    ,gamedaySceneJSON ,gamedayResultsJSON, gamedayCourtsJSON]

encounterDict = {'TennisCourtTrainEncounters':['s003a','s003b']}

#Teammate database
tm1 = {'id':'tm001'
    ,'name':'Nami'
    ,'year':2015
    ,'grades':75
    ,'skill':2
    ,'energy':'default'
    ,'heart':'normal'}
tm2 = {'id':'tm002'
    ,'name':'Vicky'
    ,'year':2015
    ,'grades':75
    ,'skill':2
    ,'energy':'default'
    ,'heart':'normal'}
tm3 = {'id':'tm003'
    ,'name':'Haruhi'
    ,'year':2015
    ,'grades':75
    ,'skill':2
    ,'energy':'default'
    ,'heart':'normal'}
tm4 = {'id':'tm004'
    ,'name':'Yuna'
    ,'year':2015
    ,'grades':75
    ,'skill':2
    ,'energy':'default'
    ,'heart':'normal'}

teammatesList = [tm1, tm2, tm3, tm4]

#Opponents
OpponentTeam1 = {'id':'schl001'
    ,'name':'Salt Academy'
    ,'teammates':[]
    }

opponentList = [OpponentTeam1]

playerTeamJSON = {'id':'schl000'
    ,'name':'Pepper Academy'
    ,'teammates':teammatesList
    }

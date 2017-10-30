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
    ,'actions':{'nav':'s003a'}}
btnGym = {'id':'btnGym'
    ,'title':'Gym'
    ,'actions':{'nav':'s004'}}
#I Don't want a different advance button for every encounter
btnAdvance = {'id':'btnAdvance'
    ,'title':'Advance'
    ,'actions':{'nav':'s002','day++':1}}
btnGameday = {'id':'btnGameday'
    ,'title':'Game Day'
    ,'actions':{'nav':'s005a'}}

buttonJSON = [btnStart,btnBack,btnTennisCourt,btnTennisCourtTrain,btnGym,btnAdvance,btnGameday]

#Scene JSONs
startSceneJSON = {'id':'s001'
    ,'buttons':['btnStart']
    ,'background':None
    ,'titleCard':'Start'
    ,'advance':None
    ,'textParagraph':None} #'background':'./Art...'
mainSceneJSON = {'id':'s002'
    ,'buttons':['btnGym','btnTennisCourt']
    ,'background':None
    ,'titleCard':'Main'
    ,'advance':None
    ,'textParagraph':None} #'background':'./Art...'
gymSceneJSON = {'id':'s004'
    ,'buttons':['btnBack']
    ,'background':None
    ,'titleCard':'Gymnasium'
    ,'advance':None
    ,'textParagraph':None}
tennisCourtsSceneJSON = {'id':'s003'
    ,'buttons':['btnTennisCourtTrain','btnBack']
    ,'background':r'Art\SoftTennis3Scaled.png'
    ,'titleCard':'Tennis Courts'
    ,'advance':None
    ,'textParagraph':None}
tennisCourtsEncounterJSON = {'id':'s003a'
    ,'buttons':[]
    ,'background':None
    ,'titleCard':None
    ,'advance':{'nav':'s002','incrementDay':1}
    ,'textParagraph':"You run the team through a set of training drills. A few hours pass as you run the team through a series of drills until they're fully exhausted"}
gamedaySceneJSON = {'id':'s005'
    ,'buttons':['btnGameday']
    ,'background':None
    ,'titleCard':'Game Day'
    ,'advance':None
    ,'textParagraph':None}
gamedayEncounterJSON = {'id':'s005a'
    ,'buttons':[]
    ,'background':None
    ,'titleCard':None
    ,'advance':{'nav':'s002','incrementDay':1}
    ,'textParagraph':"Your team competes and wins!"}

sceneJSON = [startSceneJSON,mainSceneJSON,gymSceneJSON,tennisCourtsSceneJSON,tennisCourtsEncounterJSON,gamedaySceneJSON,gamedayEncounterJSON]

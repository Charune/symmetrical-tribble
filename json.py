#Button JSONs
btnStart = {'title':'Start','actions':{'nav':'s002'}}
btnBack = {'title':'Back','actions':{'nav':'s002'}}
btnTennisCourt = {'title':'Tennis Courts','actions':{'nav':'s003'}}
btnTennisCourtTrain = {'title':'Train','actions':{'nav':'s002','day++':1}}
btnGym = {'title':'Gym','actions':{'nav':'s004'}}


buttonJSON = [btnStart,btnBack,btnTennisCourt,btnTennisCourtTrain,btnGym]

#TODO: change the button list to use the button full names not their titles (to avoid confusion later)
#Scene JSONs
startSceneJSON = {'id':'s001','buttons':['Start'],'background':'NULL','titleCard':'Start'} #'background':'./Art...'
mainSceneJSON = {'id':'s002','buttons':['Gym','Tennis Courts'],'background':'NULL','titleCard':'Main'} #'background':'./Art...'
gymSceneJSON = {'id':'s004','buttons':['Back'],'background':'NULL','titleCard':'Gymnasium'}
tennisCourtsSceneJSON = {'id':'s003','buttons':['Train','Back'],'background':r'Art\SoftTennis3Scaled.png','titleCard':'Tennis Courts'}

sceneJSON = [startSceneJSON,mainSceneJSON,gymSceneJSON,tennisCourtsSceneJSON]

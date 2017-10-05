#Button JSONs
btnStart = {'title':'Start','actionType':'nav','actionValue':'s002','center':(400,500)}
btnTennisCourt = {'title':'Tennis Courts','actionType':'nav','actionValue':'s003','center':(200,500)}
btnGym = {'title':'Gym','actionType':'nav','actionValue':'s004','center':(400,500)}
btnBack = {'title':'Back','actionType':'nav','actionValue':'s002','center':(200,200)}

buttonJSON = [btnStart,btnTennisCourt,btnGym,btnBack]

#Scene JSONs
startSceneJSON = {'id':'s001','buttons':['Start'],'background':'NULL','titleCard':'Start'} #'background':'./Art...'
mainSceneJSON = {'id':'s002','buttons':['Gym','Tennis Courts'],'background':'NULL','titleCard':'Main'} #'background':'./Art...'
gymSceneJSON = {'id':'s004','buttons':['Back'],'background':'NULL','titleCard':'Gymnasium'}
tennisCourtsSceneJSON = {'id':'s003','buttons':['Back'],'background':r'Art\SoftTennis3Scaled.png','titleCard':'Tennis Courts'}

#Final JSON
sceneJSON = [startSceneJSON,mainSceneJSON,gymSceneJSON,tennisCourtsSceneJSON]

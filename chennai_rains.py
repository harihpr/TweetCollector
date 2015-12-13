import os, time
import tweepy as tp
from tweepy import OAuthHandler
import plivo
 
consumer_key = 'XXX'
consumer_secret = 'XXX'
access_token = 'XXX'
access_secret = 'XXX'

auth_id = 'XXX'
auth_token = 'XXX'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
tpApi = tp.API(auth)
plivoClient = plivo.RestAPI(auth_id, auth_token)

messageParams = {
    'src': '+13306806958',
    'dst' : '+919940017443<+919677105393<+919220092200<+919500042887', #'919500042887'
    'text' : 'Hello, how are you?',
}

sinceId = None
for file in os.listdir('E:\HelpChennai'):
    if file.endswith('.txt'):
        sinceId = file.split('.')[0]
        os.remove('E:\HelpChennai'+'\\'+file)

messages = ''
for tweet in tp.Cursor(tpApi.search, q='#ChennaiRainsHelp+AND+help', since_id=sinceId).items(15):
    messages = messages+str(tweet.text.encode('utf-8'))+'\n'

sinceId = tweet.id
print (messages)
print (sinceId)

fo = open('E:\HelpChennai'+'\\'+str(sinceId)+'.txt', 'w')
fo.write(messages)
fo.close()

messageBody = ''
iterator = 0
fo = open('E:\HelpChennai'+'\\'+str(sinceId)+'.txt', 'r')
for line in fo.readlines():
    if iterator<5:
        messageBody = messageBody+line
        iterator += 1
    else:
        print (messageBody+'\nSent by volunteers from US\n')
        messageParams['text'] = messageBody
        response = plivoClient.send_message(messageParams)
        print (response)
        messageBody=''
        iterator = 0
        time.sleep(300)
fo.close()

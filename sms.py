import requests 
import json

# apikey = 'oJNZjI40Lrc-uiYsESGhZFBELs3U0vTUdWVh9Hznqm'
# sender = 'TXTLCL'
# def send(message, numbers):
#     PARAMS = {'apikey': apikey, 'numbers': numbers, 'message' : message, 'sender': sender}
#     UI_URL = 'https://api.textlocal.in/send/'
#     res = requests.post(url = UI_URL, data = PARAMS) 
#     r = json.loads(res.text)
#     print(r.status)
#     return (r)

# send("Test",[7021513100])
# http://api.msg91.com/api/sendhttp.php


authkey = '268968AzC9E2X1L5c968c18'
sender = 'SOCKET'
route = '4'
country = '91'
def send(message, mobiles):
    PARAMS = {'sender': sender, 'route': route, 'country' : country, 'message': message, 'mobiles': mobiles, 'authkey': authkey}
    UI_URL = 'http://api.msg91.com/api/sendhttp.php'
    # HEADERS = {'authkey': apikey, 'content-type': 'application/json'}
    res = requests.get(url = UI_URL, params = PARAMS) 
    # r = json.loads(res.text)
    print(res)
    return (res)


# send('Test SMS 3','8879799396')

  
# resp, code = sendSMS('oJNZjI40Lrc-s3L2EXFyQ6NkqXBPNjzKdbHF55TVp1', '918879366022','TXTLCL', 'From Pratik, Message send using python. Tell me if u get this sms.')
# print (resp)
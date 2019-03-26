import time
import os
import json
import requests 

compare = "https:"
UI_URL = "http://mehendicreation.com/randomain.php"
postedurl = ""

while True:
    time.sleep(1)
    try:
        os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")

        with open('tunnels.json') as data_file:    
            datajson = json.load(data_file)

        for i in datajson['tunnels']:
            url = i['public_url']
            if url[0: len(compare)] == compare:
                if url != postedurl:
                    #POST Request to server containing random url 'url' 
                    PARAMS = {'url':url} 
                    r = requests.post(url = UI_URL, data = PARAMS) 
                    data = r 
                    print(data)  
                    print(url)
                    postedurl = url

    except:
        print("No")

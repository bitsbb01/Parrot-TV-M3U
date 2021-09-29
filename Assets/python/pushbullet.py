import requests
import json
import os
from datetime import datetime
from Assets.python.time import tz
from Assets.python.dev import replitMode



if replitMode == False:
    from Auth.auth import pbapi
    pushBulletAPI = str(pbapi)
    devId = "Device"
elif replitMode == True:
    pushBulletAPI = str(os.environ['pbapi'])
    devId = "Replit"

now = datetime.now(tz)
time = now.strftime("%H:%M:%S")
 

def pushbulletMode(mode):
    def pushbulletSend(title, body):
    
        msg = {"type": "note", "title": title, "body": body}
        resp = requests.post('https://api.pushbullet.com/v2/pushes',
                            data=json.dumps(msg),
                            headers={'Authorization': 'Bearer ' + pushBulletAPI,
                                    'Content-Type': 'application/json'})
        if resp.status_code != 200:
            raise Exception('Error', resp.status_code)
        else:
            print("Send " + "'" + top + " " + mid + "'")
    
    
    top = time + " ParrotBOT"


    if str(mode) == str(1):
        mid = "Pushed into repo! - with EPG"
    elif str(mode) == str(2):
        mid = "Pushed into repo!"
    elif str(mode) == str(3):
        mid = "Just pushed into repo! - Without playlist update!"
    elif str(mode) == str(4):
        mid = "Pulled From Repo on " + devId
    elif str(mode) == str(5):
        mid = "Auto-updated M3U Links!"
    else:
        mid = "ERROR - 0001"

    pushbulletSend(top, mid)
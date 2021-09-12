import requests
import json
from datetime import datetime
from Auth.auth import pushBulletAPI
from Assets.python.time import tz
from make import madeEPG

now = datetime.now(tz)
time = now.strftime("%H:%M:%S")
 
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

if madeEPG == True:
    mid = "Pushed into repo! - with EPG"
else:
    mid = "Pushed into repo!"

pushbulletSend(top, mid)
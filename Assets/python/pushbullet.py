import requests
import json
from datetime import datetime
from Auth.auth import pushBulletAPI
from Assets.python.time import tz

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
        print("Send " + top + " " + mid)
 
 
top = time + " ParrotBOT"
mid = "Pushed into repo!"

pushbulletSend(top, mid)
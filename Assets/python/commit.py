from Assets.python.time import tz
from datetime import datetime
from Assets.python.dev import replitMode

now = datetime.now(tz)
time = now.strftime("%H:%M:%S")


msg = "'" + str(time) + " - Parrot BOT: Pushed into repo!" + "'"

if replitMode == True:
    commit = "git commit -m " + msg
elif replitMode == False:
     commit = "sudo git commit -m " + msg
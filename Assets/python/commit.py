from Assets.python.time import tz
from datetime import datetime

now = datetime.now(tz)
time = now.strftime("%H:%M:%S")


msg = "'" + str(time) + " - Parrot BOT: Pushed into repo!" + "'"
commit = "git commit -m " + msg
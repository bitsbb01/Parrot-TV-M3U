from datetime import datetime
import pytz

tz = pytz.timezone('Etc/GMT-11')

def recheckTime():
    now = datetime.now(tz)
    global time
    time = now.strftime("%H:%M")

recheckTime()



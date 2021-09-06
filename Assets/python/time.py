from datetime import datetime
import pytz

tz = pytz.timezone('Etc/GMT-11')


now = datetime.now(tz)
time = now.strftime("%H:%M")

def recheckTime():
    print("\n")
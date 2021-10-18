from make import Clear, getUSTVGO, MakeCS, MakeEng, MakeMain, Git, remPYC, RemoveMode2, MakeMainBeta, MakeEngBeta
from Assets.python.replace import replace
from keep_alive import keep_alive
from Assets.python.dev import replitMode
import time
import os

try:
    from Auth.auth import gitToken, Email, name, gitRepo
    if not gitRepo == "False":
        token = str(os.environ['gitToken'])
        email = str(os.environ['Email'])
        name = str(os.environ['name'])
        repo = str(os.environ['gitRepo'])
        origin = "sudo git remote set-url origin https://github:" + str(token) + str(repo) # Gets token and repo from Auth/auth.py
        config_mail = "sudo git config --global user.email " + email
        config_name = "sudo git config --global user.name " + name
    str(origin)
except ModuleNotFoundError:
    if not gitRepo == "False":
        token = str(os.environ['gitToken'])
        email = str(os.environ['Email'])
        name = str(os.environ['name'])
        repo = str(os.environ['gitRepo'])
        origin = "sudo git remote set-url origin https://github:" + str(token) + str(repo) # Gets token and repo from Auth/auth.py
        config_mail = "sudo git config --global user.email " + email
        config_name = "sudo git config --global user.name " + name
    str(origin)



def echo(msg):
    echocmd = "echo " + '"' + msg + '"'
    os.system(echocmd)

auto = True
timeoutTime = 7200
int(timeoutTime)

msg = "Timeout time is: " + str(timeoutTime)

echo(msg)

def Main():
    RemoveMode2()
    Clear()
    getUSTVGO()
    replace('Assets/USTVGOreplace/find.txt', 'Assets/USTVGOreplace/replace.txt', 'Assets/USTVGOreplace/data.txt', 'Assets/Channels/US/ustvgo.m3u')
    MakeCS()
    MakeEng()
    MakeMain()
    MakeMainBeta()
    MakeEngBeta()
    if gitToken == "False" and gitRepo == "False":
        Git()
    remPYC()
    
if replitMode == True:
    keep_alive()

while auto == True:
    Main()
    echo("Waiting " + str(timeoutTime) + "Seconds")
    time.sleep(int(timeoutTime))

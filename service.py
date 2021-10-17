from make import Clear, getUSTVGO, replaceUStVicons, MakeCS, MakeEng, MakeMain, Git, remPYC, RemoveMode2, MakeMainBeta, MakeEngBeta, MakePriv
from keep_alive import keep_alive
from Assets.python.dev import replitMode
import time
import os

if replitMode == False:
    from Auth.auth import gitToken, Email, name, gitRepo
    token = str(gitToken)
    email = str(Email)
    name = str(name)
    repo = str(gitRepo)
elif replitMode == True:
    token = str(os.environ['gitToken'])
    email = str(os.environ['Email'])
    name = str(os.environ['name'])
    repo = str(os.environ['gitRepo'])

origin = "git remote set-url origin https://github:" + str(token) + str(repo)
config_mail = "git config --global user.email " + email
config_name = "git config --global user.name " + name


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
    replaceUStVicons()
    MakeCS()
    MakeEng()
    MakeMain()
    MakeMainBeta()
    MakeEngBeta()
    MakePriv()
    Git()
    #pushbulletMode(5)
    remPYC()
    

keep_alive()

while auto == True:
    Main()
    echo("Waiting " + str(timeoutTime) + "Seconds")
    time.sleep(int(timeoutTime))

from make import Clear, getUSTVGO, replaceUStVicons, MakeCS, MakeEng, MakeMain, Git, pushbulletMode, remPYC, RemoveMode2
from Auth.auth import name, Email, gitToken, gitRepo
import time
import os

token = gitToken
repo = gitRepo
email = Email

origin = "sudo git remote set-url origin https://github:" + str(token) + str(repo)
config_mail = "sudo git config --global user.email " + email
config_name = "sudo git config --global user.name " + name


def echo(msg):
    echocmd = "sudo echo " + '"' + msg + '"'
    os.system(echocmd)

auto = True
timeoutTime = open('Assets/Service/timeou.txt').read()
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
    Git()
    pushbulletMode(5)
    remPYC()
    

while auto == True:
    Main()
    echo("Waiting" + str(timeoutTime)
    time.sleep(int(timeoutTime))

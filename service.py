from requests.models import MissingSchema
from make import Clear, getUSTVGO, replaceUStVicons, MakeCS, MakeEng, MakeMain, Git, pushbulletMode, remPYC, RemoveMode2
from Auth.auth import name, Email, gitToken, gitRepo
import time

token = gitToken
repo = gitRepo
email = Email

origin = "sudo git remote set-url origin https://github:" + str(token) + str(repo)
config_mail = "sudo git config --global user.email " + email
config_name = "sudo git config --global user.name " + name


auto = True
timeoutTime = 10800 #in Seconds


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
    time.sleep(timeoutTime)

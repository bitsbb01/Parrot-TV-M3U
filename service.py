import os
from make import Clear, getUSTVGO, replaceUStVicons, MakeCS, MakeEng, MakeMain, Git, pushbulletMode, remPYC, RemoveMode2
from Auth.auth import name, Email, gitToken, gitRepo

token = gitToken
repo = gitRepo
email = Email

origin = "sudo git remote set-url origin https://github:" + str(token) + str(repo) # Gets token and repo from Auth/auth.py
config_mail = "sudo git config --global user.email " + email
config_name = "sudo git config --global user.name " + name



def Mode2():
    RemoveMode2()
    Clear()
    getUSTVGO()
    replaceUStVicons()
    MakeCS()
    MakeEng()
    MakeMain()
    Git()
    pushbulletMode(2)
    remPYC()
    

Mode2()
import os

def echo(msg):
    echocmd = "sudo echo " + '"' + msg + '"'
    os.system(echocmd)
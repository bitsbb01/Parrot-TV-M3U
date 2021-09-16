import os
import shutil

if os.path.exists("Auth"):
    print("Path Exists")
else:
    os.mkdir("Auth/")
    open('Auth/auth.py', 'w')
    open('Auth/auth.py', 'w').close()

    nl = "\n"

    tk = input("Enter GH Token: ")
    rep = input("Enter repo (ex. @github.com/ParrotDevelopers/Parrot-TV-M3U.git): ")
    em = input("Enter GH Email: ")
    nm = input("Enter name: ")
    pba = input("Enter PushBullet API Key: ")

    token = "token = " + tk + nl
    repo = "repo = " + rep + nl
    email = "email = " + em + nl
    name = "name = " + nm + nl
    pba = "pushBulletAPI = " + pba

    data = token + repo + email + name + pba
    

    with open('Auth/auth.py', 'w') as fp:
        fp.write(data)
    
    fp.close()
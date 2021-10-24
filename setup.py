import os,sys

from make import Clear

os.system("pip install -r requirements.txt")

if os.path.exists('Auth/auth.py'):
    os.system("clear")
    ex = input(" Path exists, should i remove it? [Y/n]")

    if ex == "Y":
        os.system("rm Auth/auth.py")
    if ex == "y":
        os.system("rm Auth/auth.py")
    if ex == "N":
        sys.exit()
    if ex == "n":
        sys.exit()
    else:
        os.system("clear")
        print("Invalid option, bye!")
        sys.exit()
else:
    os.system("clear")
    tk = input("GH Token: ")
    em = input("GH Email: ")
    rp = input("GH Repo (Example: github.com/ParrotDevelopers/Parrot-TV-M3U.git): ")
    nm = input("Name: ")
    papi = input("Pushbullet API Key: ")

    data1 = 'gitToken = ' + '"' + tk + '"'
    data2 = 'gitRepo = ' + '"' + "@" + rp + '"'
    data3 = 'Email = ' + '"'  + em + '"'
    data4 = 'name = ' + '"'  + nm + '"'

    data = data1 + "\n" + data2 + "\n" + data3 + "\n" + data4

    os.system("clear")

    with open('Auth/auth.py', 'w') as file:
        file.write(data)
        file.close()

    Clear()
    r = input("Do u want to use this in replit? [Y/n]")
    if r == "Y" or r == "y":
        os.remove('Assets/Dev/Replit.txt')
        open('Assets/Dev/Replit.txt', 'w').write("True")
    if r == "N" or r == "n":
        os.remove('Assets/Dev/Replit.txt')
        open('Assets/Dev/Replit.txt', 'w').write("False")
    else:
        print("Invalid option, exitting!")
        sys.exit()

    Clear()
    p = input("Do u want to use proxy? [Y/n]")
    if p == "Y" or p == "y":
        os.remove('Assets/Dev/Proxy.txt')
        open('Assets/Dev/Proxy.txt', 'w').write("True")
    if p == "N" or p == "n":
        os.remove('Assets/Dev/Proxy.txt')
        open('Assets/Dev/Proxy.txt', 'w').write("False")
    else:
        print("Invalid option, exitting!")
        sys.exit()


    Clear()
    bl = input("Do u want to set custom Beta/ location? [Y/n]")
    if bl == "Y" or bl == "y":
        Clear()
        os.remove('Assets/Dev/BetaLoc.txt')
        loc = input("Enter new location for Beta/ (ex. USTVGO/)")
        open('Assets/Dev/BetaLoc.txt', 'w').write(loc)
    else:
        print("OK!")


    print("DONE!")
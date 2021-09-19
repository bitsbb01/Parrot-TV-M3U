import os,sys

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
    data5 = 'pbapi = ' + '"' + papi + '"'

    data = data1 + "\n" + data2 + "\n" + data3 + "\n" +data4 + "\n" + data5

    os.system("clear")

    with open('Auth/auth.py', 'w') as file:
        file.write(data)
        file.close()

    print("DONE!")
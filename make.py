from Assets.python.dev import replitMode
from Assets.python.proxy import proxies
from Assets.python.merge import merge
from Assets.python.commit import commit
from Assets.python.time import tz
from Assets.python.replace import replace
from Assets.python.remPYC import remPYC
from datetime import datetime
import sys
import os

try:
    from Auth.auth import gitToken, Email, name, gitRepo
    token = str(gitToken)
    email = str(Email)
    name = str(name)
    repo = str(gitRepo)
    if not repo == "False":
        origin = "sudo git remote set-url origin https://github:" + str(token) + str(repo) # Gets token and repo from Auth/auth.py
        config_mail = "sudo git config --global user.email " + email
        config_name = "sudo git config --global user.name " + name
except ModuleNotFoundError:
    token = str(os.environ['gitToken'])
    email = str(os.environ['Email'])
    name = str(os.environ['name'])
    repo = str(os.environ['gitRepo'])
    if not repo == "False":
        origin = "git remote set-url origin https://github:" + str(token) + str(repo) # Gets token and repo from Auth/auth.py
        config_mail = "git config --global user.email " + email
        config_name = "git config --global user.name " + name

proxy_mode = ""

if open('Assets/Dev/Proxy.txt', 'r').read() == "True":
    proxy_mode = True
else:
    proxy_mode = False

def done(happ):
    now = datetime.now(tz)
    time = now.strftime("%H:%M:%S")

    if happ == "pull":
        print("[" + time + "] Pulled from Repo!")
    elif happ == "push":
        print("[" + time + "] Just pushed into Repo!")
    else:
        print("[" + time + "] Playlist is up and running!")
    sys.exit()

def Clear(): # Clears Terminal
    os.system("cls")
    os.system("clear")

def getUSTVGO(): # Gets USTVGO.tv Channels
    windows = False
    python = 'python3'

    now = datetime.now(tz)
    time = now.strftime("%H:%M:%S")
        
    print('[' + time + '] Checking dependencies...')
    while True:
        try:
            import requests
            from tqdm import tqdm
            break
        except ModuleNotFoundError as e:
            module = str(e)[17:-1]

            now = datetime.now(tz)
            time = now.strftime("%H:%M:%S")

            print(f'[' + time + '] Installing {module} module for python')
            #os.system(f'{python} -m pip install --upgrade pip')
            try:
                if os.system(f'{python} -m pip install {module}') != 0:
                    print("Error")
            except:
                print(f'[!] Error installing "{module}" module. Do you have pip installed?')
                input(f'[!] Playlist generation failed. Press Ctrl+C to exit...')
                done()

    def grab(name, code, logo):
        data = {'stream': code}
        if proxy_mode == True:
            m3u = s.post('https://ustvgo.tv/data.php', data=data, proxies=proxies).text
        else:
            m3u = s.post('https://ustvgo.tv/data.php', data=data).text
        playlist.write(f'\n#EXTINF:-1 tvg-id="{code}" group-title="US Channels" tvg-logo="{logo}",USTVGO: US: {name}')
        playlist.write(f'\n{m3u}')

    total = 0
    with open('Assets/USTVGO.txt') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('~~'):
                continue
            total += 1

    s = requests.Session()
    with open('Assets/USTVGO.txt') as file:
        with open('Assets/USTVGOreplace/data.txt', 'w') as playlist:

            now = datetime.now(tz)
            time = now.strftime("%H:%M:%S")

            print('[' + time + '] Generating your playlist, please wait...\n')
            pbar = tqdm(total=total)
            for line in file:
                line = line.strip()
                if not line or line.startswith('~~'):
                    continue
                line = line.split('|')
                name = line[0].strip()
                code = line[1].strip()
                logo = line[2].strip()
                pbar.update(1)
                grab(name, code, logo)
            pbar.close()
            print('\n[SUCCESS] Playlist is generated!\n')



           
def RemoveMode1(): # Removes files so they can be Re-written
    if os.path.exists("Czechoslovaia.m3u"):
        os.remove("Czechoslovaia.m3u")

    if os.path.exists("English.m3u"):
        os.remove("English.m3u")

    if os.path.exists("Main.m3u"):
        os.remove("Main.m3u")

    if os.path.exists("Assets/Channels/US/ustvgo.m3u"):
        os.remove("Assets/Channels/US/ustvgo.m3u")

    if os.path.exists("Assets/USTVGOreplace/data.txt"):
        os.remove("Assets/USTVGOreplace/data.txt")



def MakeCS(): # Makes CZ & SK Channels 
    data = data2 = data3 = data4 = data5 = data6 = data7 = data8 = data9 = data10 = data11 = data12 = data13 = data14 = data15 = data16 = ""


    with open('Assets/Channels/SK Channels.m3u') as fp:
        data = fp.read()

    with open('Assets/Channels/CZ Channels.m3u') as fp:
        data2 = fp.read()

    with open('Assets/Channels/UK/UK Channels.m3u') as fp:
        data3 = fp.read()

    with open('Assets/Channels/US/US Channels.m3u') as fp:
        data4 = fp.read()

    with open('Assets/Channels/US/Pluto TV.m3u') as fp:
        data5 = fp.read()

    with open('Assets/Channels/US/Plex.m3u') as fp:
        data6 = fp.read()

    with open('Assets/Channels/US/xumoTV.m3u') as fp:
        data7 = fp.read()

    with open('Assets/Channels/US/Imdb.m3u') as fp:
        data8 = fp.read()

    with open('Assets/Channels/US/Roku.m3u') as fp:
        data9 = fp.read()

    with open('Assets/Channels/US/Samsung.m3u') as fp:
        data10 = fp.read()

    with open('Assets/Channels/US/Bumblebee.m3u') as fp:
        data11 = fp.read()

    with open('Assets/Channels/US/RedBox.m3u') as fp:
        data12 = fp.read()

    with open('Assets/Channels/US/Tubi.m3u') as fp:
        data13 = fp.read()

    with open('Assets/Channels/US/Vizio.m3u') as fp:
        data14 = fp.read()

    with open('Assets/Channels/US/teleup.m3u') as fp:
        data15 = fp.read()   

    with open('Assets/Channels/CA/CA Channels.m3u') as fp:
        data16 = fp.read()   
      
  

    data = "#EXTM3U \n \n" + data + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data14 + data15 + data16
    data += "\n"

  
    with open ('Czechoslovaia.m3u', 'w') as fp:
        fp.write(data)

def MakeEng(): # Makes English Only Channels
    data = data2 = data3 = data4 = data5 = data6 = data7 = data8 = data9 = data10 = data11 = data12 = data13 = data14 = ""
  

    with open('Assets/Channels/UK/UK Channels.m3u') as fp:
        data = fp.read()

    with open('Assets/Channels/US/US Channels.m3u') as fp:
        data2 = fp.read()

    with open('Assets/Channels/US/Pluto TV.m3u') as fp:
        data3 = fp.read()


    with open('Assets/Channels/US/Plex.m3u') as fp:
        data4 = fp.read()

    with open('Assets/Channels/US/xumoTV.m3u') as fp:
        data5 = fp.read()

    with open('Assets/Channels/US/Imdb.m3u') as fp:
        data6 = fp.read()

    with open('Assets/Channels/US/Roku.m3u') as fp:
        data7 = fp.read()

    with open('Assets/Channels/US/Samsung.m3u') as fp:
        data8 = fp.read()

    with open('Assets/Channels/US/Bumblebee.m3u') as fp:
        data9 = fp.read()

    with open('Assets/Channels/US/RedBox.m3u') as fp:
        data10 = fp.read()

    with open('Assets/Channels/US/Tubi.m3u') as fp:
        data11 = fp.read()

    with open('Assets/Channels/US/Vizio.m3u') as fp:
        data12 = fp.read()

    with open('Assets/Channels/US/teleup.m3u') as fp:
        data13 = fp.read()    

    with open('Assets/Channels/CA/CA Channels.m3u') as fp:
        data14 = fp.read()             



    data = "#EXTM3U \n \n" + data + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data14
    data += "\n"

  
    with open ('English.m3u', 'w') as fp:
        fp.write(data)

def MakeMain(): # Makes Main Channels
    data = data2 = data3 = data4 = data5 = data6 = data7 = data8 = data9 = data10 = data11 = data12 = data13 = data14 = data15 = data16 = data17 = data18 = ""

    with open('Assets/Channels/SK Channels.m3u') as fp:
        data = fp.read()
  
    with open('Assets/Channels/CZ Channels.m3u') as fp:
        data2 = fp.read()

    with open('Assets/Channels/UK/UK Channels.m3u') as fp:
        data3 = fp.read()

    with open('Assets/Channels/RO Channels.m3u') as fp:
        data4 = fp.read()

    with open('Assets/Channels/DE Channels.m3u') as fp:
        data5 = fp.read()

    with open('Assets/Channels/US/US Channels.m3u') as fp:
        data6 = fp.read()

    with open('Assets/Channels/US/Pluto TV.m3u') as fp:
        data7 = fp.read()

    with open('Assets/Channels/US/Plex.m3u') as fp:
        data8 = fp.read()

    with open('Assets/Channels/US/xumoTV.m3u') as fp:
        data9 = fp.read()

    with open('Assets/Channels/US/Imdb.m3u') as fp:
        data10 = fp.read()

    with open('Assets/Channels/US/Roku.m3u') as fp:
        data11 = fp.read()

    with open('Assets/Channels/US/Samsung.m3u') as fp:
        data12 = fp.read()

    with open('Assets/Channels/US/Bumblebee.m3u') as fp:
        data13 = fp.read()

    with open('Assets/Channels/US/RedBox.m3u') as fp:
        data14 = fp.read()

    with open('Assets/Channels/US/Tubi.m3u') as fp:
        data15 = fp.read()

    with open('Assets/Channels/US/Vizio.m3u') as fp:
        data16 = fp.read()

    with open('Assets/Channels/US/teleup.m3u') as fp:
        data17 = fp.read()   

    with open('Assets/Channels/CA/CA Channels.m3u') as fp:
        data18 = fp.read()   
        

    data = "#EXTM3U \n \n" + data + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data14 + data15 + data16 + data17 + data18
    data += "\n"

  
    with open ('Main.m3u', 'w') as fp:
        fp.write(data)

def MakeEngBeta(): # Makes English Only Channels
    data = data2 = data3 = data4 = data5 = data6 = data7 = data8 = data9 = data10 = data11 = data12 = data13 = data14 = data15 = ""
  

    with open('Assets/Channels/UK/UK Channels.m3u') as fp:
        data = fp.read()

    with open('Assets/Channels/US/ustvgo.m3u') as fp:
        data2 = fp.read()

    with open('Assets/Channels/US/US Channels.m3u') as fp:
        data3 = fp.read()

    with open('Assets/Channels/US/Pluto TV.m3u') as fp:
        data4 = fp.read()


    with open('Assets/Channels/US/Plex.m3u') as fp:
        data5 = fp.read()

    with open('Assets/Channels/US/xumoTV.m3u') as fp:
        data6 = fp.read()

    with open('Assets/Channels/US/Imdb.m3u') as fp:
        data7 = fp.read()

    with open('Assets/Channels/US/Roku.m3u') as fp:
        data8 = fp.read()

    with open('Assets/Channels/US/Samsung.m3u') as fp:
        data9 = fp.read()

    with open('Assets/Channels/US/Bumblebee.m3u') as fp:
        data10 = fp.read()

    with open('Assets/Channels/US/RedBox.m3u') as fp:
        data11 = fp.read()

    with open('Assets/Channels/US/Tubi.m3u') as fp:
        data12 = fp.read()

    with open('Assets/Channels/US/Vizio.m3u') as fp:
        data13 = fp.read()

    with open('Assets/Channels/US/teleup.m3u') as fp:
        data14 = fp.read()    

    with open('Assets/Channels/CA/CA Channels.m3u') as fp:
        data15 = fp.read()             



    data = "#EXTM3U \n \n" + data + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data14 + data15
    data += "\n"

    betaEngloc = open('Assets/Dev/BetaLoc.txt', 'r')
    betaEnglocFull = betaEngloc + "English.m3u"
    with open (betaEnglocFull, 'w') as fp:
        fp.write(data)

def MakeMainBeta(): # Makes Main Channels
    data = data2 = data3 = data4 = data5 = data6 = data7 = data8 = data9 = data10 = data11 = data12 = data13 = data14 = data15 = data16 = data17 = data18 = data19 = ""

    with open('Assets/Channels/SK Channels.m3u') as fp:
        data = fp.read()
  
    with open('Assets/Channels/CZ Channels.m3u') as fp:
        data2 = fp.read()

    with open('Assets/Channels/UK/UK Channels.m3u') as fp:
        data3 = fp.read()

    with open('Assets/Channels/RO Channels.m3u') as fp:
        data4 = fp.read()

    with open('Assets/Channels/DE Channels.m3u') as fp:
        data5 = fp.read()

    with open('Assets/Channels/US/ustvgo.m3u') as fp:
        data6 = fp.read()

    with open('Assets/Channels/US/US Channels.m3u') as fp:
        data7 = fp.read()

    with open('Assets/Channels/US/Pluto TV.m3u') as fp:
        data8 = fp.read()

    with open('Assets/Channels/US/Plex.m3u') as fp:
        data9 = fp.read()

    with open('Assets/Channels/US/xumoTV.m3u') as fp:
        data10 = fp.read()

    with open('Assets/Channels/US/Imdb.m3u') as fp:
        data11 = fp.read()

    with open('Assets/Channels/US/Roku.m3u') as fp:
        data12 = fp.read()

    with open('Assets/Channels/US/Samsung.m3u') as fp:
        data13 = fp.read()

    with open('Assets/Channels/US/Bumblebee.m3u') as fp:
        data14 = fp.read()

    with open('Assets/Channels/US/RedBox.m3u') as fp:
        data15 = fp.read()

    with open('Assets/Channels/US/Tubi.m3u') as fp:
        data16 = fp.read()

    with open('Assets/Channels/US/Vizio.m3u') as fp:
        data17 = fp.read()

    with open('Assets/Channels/US/teleup.m3u') as fp:
        data18 = fp.read()   

    with open('Assets/Channels/CA/CA Channels.m3u') as fp:
        data19 = fp.read()   
  

    data = "#EXTM3U \n \n" + data + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data14 + data15 + data16 + data17 + data18 + data19
    data += "\n"

    betaMainloc = open('Assets/Dev/BetaLoc.txt', 'r')
    betaMainlocFull = betaMainloc + "Main.m3u"
    with open (betaMainlocFull, 'w') as fp:
        fp.write(data)

def Git(): # Commits to GitHub Repo
    os.system(config_mail)
    os.system(config_name)
    os.system(origin)
    if replitMode == False:
        os.system("sudo git add .")
        os.system(commit)
        os.system("sudo git push")
    elif replitMode == True:
        os.system("git add .")
        os.system(commit)
        os.system("git push")

    
def Mode1():
    m = "not"
    RemoveMode1()
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
    done(m)


def Main():
    def select():
        if replitMode == False:
            Clear()
            print("###############################################")
            print("#          1.) Without EPG                    #")
            print("###############################################")

            modeST = input("Select Mode: ")

            if modeST == str(1):
                Mode1()
            elif modeST == str(5):
              os.system("python3 service.py")
            else:
                select()
        elif replitMode == True:
            os.system("python3 service.py")

    admin = os.getuid()

    if admin == 1000:
        if replitMode == False:
            os.system("clear")
            print("Superuser UwU: ")
            os.system("sudo python3 make.py")
        elif replitMode == True:
            select()

    elif admin == 0:
        select()

if __name__ == "__main__":
    Main()


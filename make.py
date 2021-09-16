import os
import time
import sys
from Auth.auth import *
from Assets.python.merge import merge
from Assets.python.commit import commit
from Assets.python.time import tz
from Assets.python.remPYC import remPYC
from Assets.python.pushbullet import pushbulletMode
from datetime import datetime



origin = "git remote set-url origin https://github:" + token + repo # Gets token and repo from Auth/auth.py
config_mail = "git config --global user.email " + email
config_name = "git config --global user.name " + name

def done():
    now = datetime.now(tz)
    time = now.strftime("%H:%M:%S")
    print("[" + time + "] Playlist is up and running!")

def Clear(): # Clears Terminal
    os.system("cls")
    os.system("clear")

def getUSTVGO(): # Gets USTVGO.tv Channels
    import os
    import sys

    windows = False
    python = 'python3'
    if 'win' in sys.platform:
        windows = True
        python = 'python'

        
    print('[*] Checking dependencies...')
    while True:
        try:
            import requests
            from tqdm import tqdm
            break
        except ModuleNotFoundError as e:
            module = str(e)[17:-1]
            print(f'[*] Installing {module} module for python')
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
        m3u = s.post('https://ustvgo.tv/data.php', data=data).text
        playlist.write(f'\n#EXTINF:-1 tvg-id="{code}" group-title="ustvgo" tvg-logo="{logo}", {name}')
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
        with open('Assets/Channels/ustvgo.m3u', 'w') as playlist:
            print('[*] Generating your playlist, please wait...\n')
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

    if os.path.exists("EPG/ustvgo_epg.xml"):
        os.remove("EPG/ustvgo_epg.xml")

    if os.path.exists("Assets/Channels/ustvgo.m3u"):
        os.remove("Assets/Channels/ustvgo.m3u")

    if os.path.exists("EPG/tvtv.us.guide.xml"):
        os.remove("EPG/tvtv.us.guide.xml")

    if os.path.exists("EPG/tvtv.us.guide.xml.1"):
        os.remove("EPG/tvtv.us.guide.xml.1")

    if os.path.exists("EPG/EPG.tar.gz"):
        os.remove("EPG/EPG.tar.gz")
           
def RemoveMode2(): # Removes files so they can be Re-written
    if os.path.exists("Czechoslovaia.m3u"):
        os.remove("Czechoslovaia.m3u")

    if os.path.exists("English.m3u"):
        os.remove("English.m3u")

    if os.path.exists("Main.m3u"):
        os.remove("Main.m3u")

    if os.path.exists("EPG/ustvgo_epg.xml"):
        os.remove("EPG/ustvgo_epg.xml")

    if os.path.exists("Assets/Channels/ustvgo.m3u"):
        os.remove("Assets/Channels/ustvgo.m3u")

def MakeCS(): # Makes CZ & SK Channels 
    data = data2 = data3 = data4 = data5 = data6 = data7 = data8 = ""
  

    with open('Assets/Channels/SK Channels.m3u') as fp:
        data = fp.read()

    with open('Assets/Channels/CZ Channels.m3u') as fp:
        data2 = fp.read()

    with open('Assets/Channels/UK Channels.m3u') as fp:
        data3 = fp.read()

    with open('Assets/Channels/US Channels.m3u') as fp:
        data4 = fp.read()

    with open('Assets/Channels/Pluto TV.m3u') as fp:
        data5 = fp.read()

    with open('Assets/Channels/ustvgo.m3u') as fp:
        data6 = fp.read()

    with open('Assets/Channels/xumoTV.m3u') as fp:
        data7 = fp.read()

    with open('Assets/Channels/Movies.m3u') as fp:
        data8 = fp.read()
  

    data = "#EXTM3U \n \n" + data + data2 + data3 + data4 + data5 + data6 + data7 + data8
    data += "\n"

  
    with open ('Czechoslovaia.m3u', 'w') as fp:
        fp.write(data)

def MakeEng(): # Makes English Only Channels
    data = data2 = data3 = data4 = data5 = ""
  

    with open('Assets/Channels/UK Channels.m3u') as fp:
        data = fp.read()
  

    with open('Assets/Channels/US Channels.m3u') as fp:
        data2 = fp.read()

    with open('Assets/Channels/Pluto TV.m3u') as fp:
        data3 = fp.read()

    with open('Assets/Channels/ustvgo.m3u') as fp:
        data4 = fp.read()

    with open('Assets/Channels/xumoTV.m3u') as fp:
        data5 = fp.read()


    data = "#EXTM3U \n \n" + data + data2 + data3 + data4 + data5
    data += "\n"

  
    with open ('English.m3u', 'w') as fp:
        fp.write(data)

def MakeMain(): # Makes Main Channels
    data = data2 = data3 = data4 = data5 = data6 = data7 = ""

    with open('Assets/Channels/SK Channels.m3u') as fp:
        data = fp.read()
  

    with open('Assets/Channels/CZ Channels.m3u') as fp:
        data2 = fp.read()

    with open('Assets/Channels/UK Channels.m3u') as fp:
        data3 = fp.read()

    with open('Assets/Channels/US Channels.m3u') as fp:
        data4 = fp.read()

    with open('Assets/Channels/Pluto TV.m3u') as fp:
        data5 = fp.read()

    with open('Assets/Channels/ustvgo.m3u') as fp:
        data6 = fp.read()

    with open('Assets/Channels/xumoTV.m3u') as fp:
        data7 = fp.read()

  

    data = "#EXTM3U \n \n" + data + data2 + data3 + data4 + data5 + data6 + data7
    data += "\n"

  
    with open ('Main.m3u', 'w') as fp:
        fp.write(data)

def Git(): # Commits to GitHub Repo
    os.system(config_mail)
    os.system(config_name)
    os.system(origin)
    os.system("git add .")
    os.system(commit)
    os.system("git push")

def Mode1(): 
    RemoveMode1()
    Clear()
    getUSTVGO()
    updateEPG()
    tar()
    MakeCS()
    MakeEng()
    MakeMain()
    time.sleep(10)
    Git()
    pushbulletMode(1)
    done()
    remPYC()
    
def Mode2():
    RemoveMode2()
    Clear()
    getUSTVGO()
    MakeCS()
    MakeEng()
    MakeMain()
    Git()
    pushbulletMode(2)
    done()
    remPYC()

def Mode3():
    Clear()
    Git()
    pushbulletMode(3)
    done()
    remPYC()

def tar():
    os.system("cp EPG/EPG.xml EPG.xml")
    os.system("tar -czvf EPG.tar.gz EPG.xml")
    os.system("mv EPG.tar.gz EPG/")
    if os.path.exists("EPG.xml"):
        os.remove("EPG.xml")

def updateEPG(): # Adds USTVGO to EPG
    os.system("wget -P EPG/ https://iptv-org.github.io/epg/guides/tvtv.us.guide.xml")
    os.system(merge)

def ReplaceIcons():
    findlines = open('Assets/ChangeIcons/find.txt').read().split('\n')
    replacelines = open('Assets/ChangeIcons/replace.txt').read().split('\n')
    find_replace = dict(zip(findlines, replacelines))

    with open('Assets/ChangeIcons/data.txt') as data:
        with open('Assets/Channels/ustvgo.m3u', 'w') as new_data:
            for line in data:
                for key in find_replace:
                    if key in line:
                        line = line.replace(key, find_replace[key])
                new_data.write(line)

def select():
    Clear()
    print("#################################################################")
    print("#          1.) With EPG                                         #")
    print("#          2.) Without EPG                                      #")
    print("#          3.) Push into GitHub Only                            #")                                 
    print("#################################################################")

    modeST = input("Select Mode: ")

    if modeST == str(1):
        Mode1()
    elif modeST == str(2):
        Mode2()
    elif modeST == str(3):
        Mode3()
    else:
        select()

admin = os.getuid()

if admin == 1000:
    os.system("clear")
    print("Superuser UwU: ")
    os.system("sudo python3 make.py")

elif admin == 0:
    select()



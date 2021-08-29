import os
import sys
from Auth.auth import *

origin = "git remote set-url origin https://github:" + token + repo # Gets token and repo from Auth/auth.py
config_mail = "git config --global user.email " + email
config_name = "git config --global user.name " + name

def Clear(): # Clears Terminal
    os.system("cls")
    os.system("clear")

def getUSTVGO(): # Gets USTVGO.tv Channels
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
                    raise 
            except:
                print(f'[!] Error installing "{module}" module. Do you have pip installed?')
                input(f'[!] Playlist generation failed. Press Ctrl+C to exit...')

    def grab(name, code, logo):
        data = {'stream': code}
        m3u = s.post('https://ustvgo.tv/data.php', data=data).text
        playlist.write(f'\n#EXTINF:-1 tvg-id="{code}" group-title="USTVGO" tvg-logo="{logo}",USTVGO: US: {name}')
        playlist.write(f'\n{m3u}')

    total = 0
    with open('Assets/USTVGO/Channel-Info.txt') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('~~'):
                continue
            total += 1

    s = requests.Session()
    with open('Assets/USTVGO/Channel-Info.txt') as file:
        with open('Assets/ChangeIcons/data.txt', 'w') as playlist:
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

def Remove(): # Removes files so they can be Re-written
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

    with open('Assets/Channels/Movies.m3u') as fp:
        data7 = fp.read()
  

    data = "#EXTM3U \n \n" + data + data2 + data3 + data4 + data5 + data6 + data7
    data += "\n"

  
    with open ('Czechoslovaia.m3u', 'w') as fp:
        fp.write(data)

def MakeEng(): # Makes English Only Channels
    data = data2 = data3 = data4 = ""
  

    with open('Assets/Channels/UK Channels.m3u') as fp:
        data = fp.read()
  

    with open('Assets/Channels/US Channels.m3u') as fp:
        data2 = fp.read()

    with open('Assets/Channels/Pluto TV.m3u') as fp:
        data3 = fp.read()

    with open('Assets/Channels/ustvgo.m3u') as fp:
        data4 = fp.read()



    data = "#EXTM3U \n \n" + data + data2 + data3 + data4
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


    with open('Assets/Channels/Movies.m3u') as fp:
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
    os.system("git commit -m 'Parrot BOT: Pushed to repo!'")
    os.system("git push")

def Runner(): # Starts all scripts
    Remove()
    Clear()
    getUSTVGO()
    ReplaceIcons()
    MakeCS()
    MakeEng()
    MakeMain()
    Git()

def updateEPG(): # Adds USTVGO to EPG
    os.system("wget -P EPG/ https://raw.githubusercontent.com/nomoney4me/ustvgo/main/output/ustvgo_epg.xml")
    os.system("python2 EPG/xml_merge.py EPG/EPG1.xml EPG/ustvgo_epg.xml > EPG/EPG.xml")


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


Runner()

print("\n")

print("[DONE] Playlist is up and running!")
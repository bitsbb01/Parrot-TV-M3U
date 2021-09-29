def Main():
    import os
    from Assets.python.dev import replitMode

    if replitMode == True:
        os.system("pip install pytz")

    import time
    import sys
    from Assets.python.merge import merge
    from Assets.python.commit import commit
    from Assets.python.time import tz
    from Assets.python.remPYC import remPYC
    from Assets.python.USTVGOreplace import replaceUStVicons
    from Assets.python.pushbullet import pushbulletMode
    from datetime import datetime


    if replitMode == False:
        from Auth.auth import gitToken, Email, name, pbapi, gitRepo
        token = str(gitToken)
        email = str(Email)
        name = str(name)
        pushBulletAPI = str(pbapi)
        repo = str(gitRepo)
    elif replitMode == True:
        token = str(os.environ['gitToken'])
        email = str(os.environ['Email'])
        name = str(os.environ['name'])
        pushBulletAPI = str(os.environ['pbapi'])
        repo = str(os.environ['gitRepo'])

    if replitMode == False:
        origin = "sudo git remote set-url origin https://github:" + str(token) + str(repo) # Gets token and repo from Auth/auth.py
        config_mail = "sudo git config --global user.email " + email
        config_name = "sudo git config --global user.name " + name
    elif replitMode == True:
        origin = "git remote set-url origin https://github:" + str(token) + str(repo) # Gets token and repo from Auth/auth.py
        config_mail = "git config --global user.email " + email
        config_name = "git config --global user.name " + name

    str(origin)

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
            m3u = s.post('https://ustvgo.tv/data.php', data=data).text
            playlist.write(f'\n#EXTINF:-1 tvg-id="{code}" group-title="USTVGO;US Channels" tvg-logo="{logo}",USTVGO: US: {name}')
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

        if os.path.exists("EPG/ustvgo_epg.xml"):
            os.remove("EPG/ustvgo_epg.xml")

        if os.path.exists("Assets/Channels/ustvgo.m3u"):
            os.remove("Assets/Channels/ustvgo.m3u")

        if os.path.exists("Assets/USTVGOreplace/data.txt"):
            os.remove("Assets/USTVGOreplace/data.txt")

        if os.path.exists("EPG/tvtv.us.guide.xml"):
            os.remove("EPG/tvtv.us.guide.xml")

        if os.path.exists("EPG/tvtv.us.guide.xml.1"):
            os.remove("EPG/tvtv.us.guide.xml.1")

        if os.path.exists("EPG/CZ.xml"):
            os.remove("EPG/CZ.xml")
            
        if os.path.exists("EPG/CZ.xml"):
            os.remove("EPG/EPG.xml")

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

        if os.path.exists("Assets/USTVGOreplace/data.txt"):
            os.remove("Assets/USTVGOreplace/data.txt")

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
        replaceUStVicons()
        updateEPG()
        tar()
        MakeCS()
        MakeEng()
        MakeMain()
        time.sleep(10)
        Git()
        pushbulletMode(1)
        remPYC()
        done(m)
        
    def Mode2():
        m = "not"
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
        done(m)

    def Mode3():
        m = "push"
        Clear()
        Git()
        pushbulletMode(3)
        remPYC()
        done(m)

    def Mode4():
        m = "pull"
        Clear()
        if replitMode == True:
            os.sytem("git pull")
        elif replitMode == False:
            os.system("sudo git pull")
        pushbulletMode(4)
        remPYC()
        done(m)

    def tar():
        os.system("cp EPG/EPG.xml EPG.xml")
        os.system("tar -czvf EPG.tar.gz EPG.xml")
        os.system("mv EPG.tar.gz EPG/")
        if os.path.exists("EPG.xml"):
            os.remove("EPG.xml")

    def updateEPG(): # Adds USTVGO to EPG
        if replitMode == False:
            os.system("wget -P EPG/ https://iptv-org.github.io/epg/guides/tvtv.us.guide.xml")
            os.system("python3 EPG/Generator/generator.py")
            os.system(merge)
        elif replitMode == True:
            print("Cannot do that in Replit!!!")

    def select():
        if replitMode == False:
            Clear()
            print("###############################################")
            print("#          1.) With EPG                       #")
            print("#          2.) Without EPG                    #")
            print("#          3.) Push into GitHub Only          #")   
            print("#          4.) Pull from GitHub               #")
            print("###############################################")

            modeST = input("Select Mode: ")

            if modeST == str(1):
                Mode1()
            elif modeST == str(2):
                Mode2()
            elif modeST == str(3):
                Mode3()
            elif modeST == str(4):
                Mode4()
            else:
                select()
        elif replitMode == True:
            Mode2()

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
import nextcord
import time
import os
import shutil
import random


from nextcord.message import Message
from nextcord.ext import commands
from Auth.auth import disToken, disUID
from make import RemoveMode1, RemoveMode2, Clear, getUSTVGO, replaceUStVicons, updateEPG, tar, MakeCS, MakeEng, MakeMain, Git, pushbulletMode

TOKEN = disToken
Admins = open('Assets/Admin/list.txt', 'r').read()
SAdmins = open('Assets/Admin/Slist.txt', 'r').read()







print("Loading!")

def echo(msg):
    echocmd = "sudo echo " + '"' + msg + '"'
    os.system(echocmd)

def remPYC():
    if os.path.exists("Auth/__pycache__"):
        shutil.rmtree("Auth/__pycache__")

    if os.path.exists("Assets/python/__pycache__"):
        shutil.rmtree("Assets/python/__pycache__")

    if os.path.exists("Assets/USTVGO/scripts/__pycache__"):
        shutil.rmtree("Assets/USTVGO/scripts/__pycache__")

    if os.path.exists("EPG/Generator/__pycache__"):
        shutil.rmtree("EPG/Generator/__pycache__")

    if os.path.exists("__pycache__"):
        shutil.rmtree("__pycache__")

def Mode1(): 
    RemoveMode1()
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
    
def Mode2():
    RemoveMode2()
    getUSTVGO()
    replaceUStVicons()
    MakeCS()
    MakeEng()
    MakeMain()
    Git()
    pushbulletMode(2)

def Mode3():
    Git()
    pushbulletMode(3)
    remPYC()


prefix = "!"
prefix2 = "&"

class MyClient(nextcord.Client):
    async def on_ready(self):
        Clear()
        print('------')
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')


    async def on_message(self, message):
        aid = message.author.id

        if aid == self.user.id:
            return
        

        """
        if message.content.startswith(prefix + 'mode1'):
            if str(aid) in (Admins):
                await message.reply('OK!')
                echo("Running Mode 1")
                Mode1()
                await message.reply("Done! - with EPG!")
            else:
                await message.reply("You don't have premissions to do that!")
        """

        if message.content.startswith('fuck you'):
            if str(message.author.id) == "534333257014050836":
                await message.reply("You're my best friend i wouldn't fuck on u :smiley:")
            else:
                await message.reply("Sry, don't have time, I'm currently in bed with ur mom.")

        if message.content.startswith(prefix + 'M3U'):
            await message.reply('OK!')
            echo("Running Mode 2:")
            Mode2()
            await message.reply("Done! - without EPG!")

        if message.content.startswith(prefix + 'resetbot'):
            if str(aid) in (Admins):
                await message.reply('Restarting BOT!')
                echo("Restarting BOT:")
                os.system("sudo systemctl restart parrotbot.discord.service")
            else:
                await message.reply("You don't have premissions to do that!")

        if message.content.startswith(prefix + 'neofetch'):
            randnum = random.randint(1, 10)
            if str(randnum) == "1":
                clrEmbed=0x08ff00
            if str(randnum) == "2":
                clrEmbed=0x00ffff
            if str(randnum) == "3":
                clrEmbed=0xfa6900
            if str(randnum) == "4":
                clrEmbed=0xf98082
            if str(randnum) == "5":
                clrEmbed=0x75edeb
            if str(randnum) == "6":
                clrEmbed=0x3d85c6
            if str(randnum) == "7":
                clrEmbed=0x0b5394
            if str(randnum) == "8":
                clrEmbed=0xaa35c
            if str(randnum) == "9":
                clrEmbed=0x4fa875
            if str(randnum) == "10":
                clrEmbed=0x43765f
            echo("Showing help message:")
            embedVar = nextcord.Embed(
            description="Neofetch: ",color=int(clrEmbed)
                    )
            embedVar.set_image(url = 'https://i.ytimg.com/vi/caBFyIyDZME/hqdefault.jpg')
            embedVar.add_field(name="APU", value="Potato gen 6")
            embedVar.add_field(name="Distro", value="Manjaro Linux")
            embedVar.add_field(name="RAM", value="4gb")
            await message.channel.send(embed=embedVar)

        if message.content.startswith(prefix + 'log'):
            if str(aid) in (Admins):
                echo("Showing System Log!")
                os.system("sudo rm -f Assets/Admin/log.sys")
                os.system("sudo systemctl status parrotbot.discord.service > Assets/Admin/log.sys")
                await message.reply(open('Assets/Admin/log.sys', 'r').read())
                os.system("sudo rm -f Assets/Admin/log.sys")
            else:
                await message.reply("You don't have premissions to do that!")



        if message.content.startswith(prefix + 'uidlog'):
            if str(aid) in (Admins):
                await message.reply(open('Assets/Admin/log.uid', 'r').read())
                echo("Showing UID Log!:")
            else:
                await message.reply("You don't have premissions to do that!")

        if message.content.startswith(prefix + 'admin'):
            if str(aid) in (Admins):
                await message.reply("You're Admin!")
            else:
                await message.reply("You're NOT Admin!")

        if message.content.startswith(prefix + 'rempyc'):
            echo("Removing Pyc:")
            await message.reply("Done! - Removed pycache")

        if message.content.startswith(prefix + 'uid'):
            if str(message.content) == prefix + "uidlog":
                echo("Shwoing uidlog")
            else:
                id =  aid
                str(id)
                os.system("sudo cp Assets/Admin/log.uid Assets/Admin/log.uid.bak")

                with open("Assets/Admin/log.uid.bak", "r") as baku:
                    bak = baku.read()
                    baku.close()

                with open('Assets/Admin/log.uid', 'w') as f:
                    write = f.write(str(bak) + "\n" + str(id))
                    f.close()

                os.system("sudo rm -f Assets/Admin/log.uid.bak")


                echo(str("Removing Showing usrid -") + str(id) + str(":"))
                await message.reply(str("Your uid: ") + str(id))

        if message.content.startswith(prefix2 + 'statusbot'):
            if str(aid) in (SAdmins):
                echo("Showing Auto-Update Log!")
                os.system("sudo rm -f Assets/Admin/log.sys")
                os.system("sudo systemctl status parrotbot.service > Assets/Admin/log-auto.sys")
                await message.reply(open('Assets/Admin/log-auto.sys', 'r').read())
                os.system("sudo rm -f Assets/Admin/log-auto.sys")
            else:
                await message.reply("You don't have premissions to do that!")

        if message.content.startswith(prefix2 + 'startbot'):
            if str(aid) in (SAdmins):
                await message.reply('Restarting BOT!')
                echo("Starting Aut-Update BOT:")
                os.system("sudo systemctl start parrotbot.service")
            else:
                await message.reply("You don't have premissions to do that!")

        if message.content.startswith(prefix2 + 'resetbot'):
            if str(aid) in (SAdmins):
                await message.reply('Restarting BOT!')
                echo("Restarting Aut-Update BOT:")
                os.system("sudo systemctl restart parrotbot.service")
            else:
                await message.reply("You don't have premissions to do that!")

        if message.content.startswith(prefix2 + 'stopbot'):
            if str(aid) in (SAdmins):
                await message.reply('Restarting BOT!')
                echo("Stopping Aut-Update BOT:")
                os.system("sudo systemctl stop parrotbot.service")
            else:
                await message.reply("You don't have premissions to do that!")

        if message.content.startswith(prefix2 + 'stt'):
            from Assets.python.STT import replaceSTT
            if str(aid) in (SAdmins):
                os.system('sudo rm -f Assets/Service/tt.txt')
                os.system('sudo rm -f Assets/Service/timeou.txt')
                timeouttime = str(message.content)
                timeouttime.replace('&stt', 'fuck')
                open('Assets/Service/tt.txt', 'w').write(timeouttime)
                replaceSTT()
                await message.reply("New auto-update timeout is now: " + timeouttime)
            else:
                await message.reply("You don't have premissions to do that!")

        if message.content.startswith(prefix2 + 'help'):
            randnum = random.randint(1, 10)
            if str(randnum) == "1":
                clrEmbed=0x08ff00
            if str(randnum) == "2":
                clrEmbed=0x00ffff
            if str(randnum) == "3":
                clrEmbed=0xfa6900
            if str(randnum) == "4":
                clrEmbed=0xf98082
            if str(randnum) == "5":
                clrEmbed=0x75edeb
            if str(randnum) == "6":
                clrEmbed=0x3d85c6
            if str(randnum) == "7":
                clrEmbed=0x0b5394
            if str(randnum) == "8":
                clrEmbed=0xaa35c
            if str(randnum) == "9":
                clrEmbed=0x4fa875
            if str(randnum) == "10":
                clrEmbed=0x43765f
            echo("Showing help message:")
            embedVar = nextcord.Embed(
            description="It looks like u need help :flushed:", color=int(clrEmbed)
                    )
            # embedVar.add_field(name="==============", value="```!mode1``` - Runs M3U Update With EPG [Admin Rquired]")
            embedVar.add_field(name="==============", value="```&statusbot``` - Gets status of Auto-Update BOT [Super Admin Required]")
            embedVar.add_field(name="==============", value="```&startbot``` - Start Auto-Update BOT [Super Admin Required]")
            embedVar.add_field(name="==============", value="```&resetbot``` - Restart Auto-Update BOT [Super Admin Required]")
            embedVar.add_field(name="==============", value="```&stopbot``` - Stop Auto-Update BOT [Super Admin Required]")
            embedVar.add_field(name="==============", value="```&stt [Number in seconds]``` - Edit timeout time between updates [Super Admin Required]")
            await message.channel.send(embed=embedVar)

        if message.content.startswith(prefix + 'help'):
            randnum = random.randint(1, 10)
            if str(randnum) == "1":
                clrEmbed=0x08ff00
            if str(randnum) == "2":
                clrEmbed=0x00ffff
            if str(randnum) == "3":
                clrEmbed=0xfa6900
            if str(randnum) == "4":
                clrEmbed=0xf98082
            if str(randnum) == "5":
                clrEmbed=0x75edeb
            if str(randnum) == "6":
                clrEmbed=0x3d85c6
            if str(randnum) == "7":
                clrEmbed=0x0b5394
            if str(randnum) == "8":
                clrEmbed=0xaa35c
            if str(randnum) == "9":
                clrEmbed=0x4fa875
            if str(randnum) == "10":
                clrEmbed=0x43765f
            echo("Showing help message:")
            embedVar = nextcord.Embed(
            description="It looks like u need help :flushed:", color=int(clrEmbed)
                    )
            # embedVar.add_field(name="==============", value="```!mode1``` - Runs M3U Update With EPG [Admin Rquired]")
            embedVar.add_field(name="==============", value="```!M3U``` - Runs M3U Update Without EPG [Admin Not Required]")
            embedVar.add_field(name="==============", value="```!rempyc``` - Removes Pycache Files [Admin Not Required]")
            embedVar.add_field(name="==============", value="```!uid``` - Shows Your UID [Admin Not Required]")
            embedVar.add_field(name="==============", value="```!resetbot``` - Restarts BOT [Admin Rquired]")
            embedVar.add_field(name="==============", value="```!log``` - View System Service Log [Admin Rquired]")
            embedVar.add_field(name="==============", value="```!uidlog``` - View UID Log [Admin Rquired]")
            embedVar.add_field(name="==============", value="```!neofetch``` - Show Neofetch [Admin Not Required]")
            await message.channel.send(embed=embedVar)

client = MyClient()
client.run(TOKEN)

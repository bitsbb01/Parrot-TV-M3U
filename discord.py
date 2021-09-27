import nextcord
import time
import os
import shutil
from Auth.auth import disToken, disUID
from make import RemoveMode1, RemoveMode2, Clear, getUSTVGO, replaceUStVicons, updateEPG, tar, MakeCS, MakeEng, MakeMain, Git, pushbulletMode

TOKEN = disToken

print("Loading!")

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

class MyClient(nextcord.Client):
    async def on_ready(self):
        Clear()
        print('------')
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith(prefix + 'mode1'):
            if str(message.author.id) == str(disUID):
                await message.reply('OK!')
                print(f"Running Mode 1:")
                Mode1()
                await message.reply("Done! - with EPG!")
            else:
                await message.reply("You don't have premissions to do that!")

        if message.content.startswith(prefix + 'mode2'):
            await message.reply('OK!')
            print(f"Running Mode 2:")
            Mode2()
            await message.reply("Done! - without EPG!")

        if message.content.startswith(prefix + 'mode3'):
            if str(message.author.id) == str(disUID):
                await message.reply('OK!')
                print(f"Running Mode 3:")
                Mode3()
                await message.reply("Done! - Just Pushed Into Repo!")
            else:
                await message.reply("You don't have premissions to do that!")

        if message.content.startswith(prefix + 'restbot'):
            if str(message.author.id) == str(disUID):
                await message.reply('Restarting BOT!')
                print(f"Restarting BOT:")
                os.system("sudo systemctl restart parrotbot.discord.service")
            else:
                await message.reply("You don't have premissions to do that!")


        if message.content.startswith(prefix + 'cls'):
            print(f"Clearing console:")
            Clear()
            await message.reply("Done! - Console is now fresh and clean!")

        if message.content.startswith(prefix + 'rempyc'):
            print(f"Removing Pyc:")
            await message.reply("Done! - Removed py")

        if message.content.startswith(prefix + 'uid'):
            id =  message.author.id
            str(id)
            #with open('uid.txt', 'w') as f: #Enable if u want to get someone's uid
                #f.write(str(id))
            print(str("Removing Showing usrid -") + str(id) + str(":"))
            await message.reply(str("Your id: ") + str(id))


        if message.content.startswith(prefix + 'help'):
            print(f"Showing help message:")
            embedVar = nextcord.Embed(
            title="Help:", description="It looks like u need help :flushed:", color=0x336EFF
                    )
            embedVar.add_field(name="Run Mode 1", value="!mode1", inline=False)
            embedVar.add_field(name="Run Mode 2", value="!mode2", inline=False)
            embedVar.add_field(name="Run Mode 3", value="!mode3", inline=False)
            embedVar.add_field(name="Clear Console", value="!cls", inline=False)
            embedVar.add_field(name="remove __pycache__", value="!rempyc", inline=False)
            embedVar.add_field(name="Show your id", value="!uid", inline=False)
            embedVar.add_field(name="Restart BOT", value="!restbot", inline=False)
            embedVar.add_field(name="Help", value="!help", inline=False)
            await message.channel.send(embed=embedVar)

client = MyClient()
client.run(TOKEN)

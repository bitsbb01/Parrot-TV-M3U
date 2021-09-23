import nextcord
import time
from Auth.auth import disToken
from make import RemoveMode1, RemoveMode2, Clear, getUSTVGO, replaceUStVicons, updateEPG, tar, MakeCS, MakeEng, MakeMain, Git, pushbulletMode, remPYC

TOKEN = disToken

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
            await message.reply('OK!')
            print(f"Running Mode 1:")
            Mode1()
            await message.reply("Done! - with EPG!")

        if message.content.startswith(prefix + 'mode2'):
            await message.reply('OK!')
            print(f"Running Mode 2:")
            Mode2()
            await message.reply("Done! - without EPG!")

        if message.content.startswith(prefix + 'mode3'):
            await message.reply('OK!')
            print(f"Running Mode 3:")
            Mode3()
            await message.reply("Done! - Just Pushed Into Repo!")

        if message.content.startswith(prefix + 'cls'):
            print(f"Clearing console:")
            Clear()
            await message.reply("Done! - Console is now fresh and clean!")

        if message.content.startswith(prefix + 'rempyc'):
            print(f"Removing Pyc:")
            await message.reply("Done! - Removed py")


        if message.content.startswith('!help'):
            print(f"Showing help message:")
            embedVar = nextcord.Embed(
            title="Help:", description="It looks like u need help :flushed:", color=0x336EFF
                    )
            embedVar.add_field(name="Run Mode 1", value="!mode1", inline=False)
            embedVar.add_field(name="Run Mode 2", value="!mode2", inline=False)
            embedVar.add_field(name="Run Mode 3", value="!mode3", inline=False)
            embedVar.add_field(name="Clear Console", value="!cls", inline=False)
            embedVar.add_field(name="remove __pycache__", value="!rempyc", inline=False)
            embedVar.add_field(name="Help", value="!help", inline=False)
            await message.channel.send(embed=embedVar)

client = MyClient()
client.run(TOKEN)

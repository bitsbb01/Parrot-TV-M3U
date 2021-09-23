import nextcord
import time
from Auth.auth import disToken
from make import RemoveMode1, RemoveMode2, Clear, getUSTVGO, replaceUStVicons, updateEPG, tar, MakeCS, MakeEng, MakeMain, Git, pushbulletMode, remPYC

TOKEN = disToken

def Mode1(): 
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
    
def Mode2():
    RemoveMode2()
    Clear()
    getUSTVGO()
    replaceUStVicons()
    MakeCS()
    MakeEng()
    MakeMain()
    Git()
    pushbulletMode(2)

def Mode3():
    Clear()
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
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith(prefix + 'mode1'):
            await message.reply('OK!')
            print(f"Running Mode 1:")
            Mode1()

        if message.content.startswith(prefix + 'mode2'):
            await message.reply('OK!')
            print(f"Running Mode 2:")
            Mode2()

        if message.content.startswith(prefix + 'mode3'):
            await message.reply('OK!')
            print(f"Running Mode 3:")
            Mode3()

        if message.content.startswith(prefix + 'cls'):
            await message.reply('Cleared Console!')
            print(f"Clearing console:")
            Clear()

        if message.content.startswith(prefix + 'rempyc'):
            await message.reply('Removed PyCache!')
            print(f"Removing Pyc:")
            Clear()

        if message.content.startswith(prefix + 'whoami'):
            await message.reply('Root!')
            print(f"You're Root:")
            Clear()

client = MyClient()
client.run(TOKEN)

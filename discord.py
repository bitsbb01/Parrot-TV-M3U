
TOKEN ="ODg3MDEzNzYzMjQzNDYyNzQ2.YT998Q.e1__gkPB324lX7pbcKvxC8V-4bc"


import nextcord
from make import Mode1, Mode2, Mode3, Mode4


prefix = "!"

class MyClient(nextcord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith(prefix + 'mode1'):
            await message.reply('Hello!')
            Mode1()

        if message.content.startswith(prefix + 'mode2'):
            await message.reply('Hello!')
            Mode2()

        if message.content.startswith(prefix + 'mode3'):
            await message.reply('Hello!')
            Mode3()

client = MyClient()
client.run(TOKEN)

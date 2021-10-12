from nextcord.ext import commands
import Assets.python.meme as meme
import typing
import os
import shutil
import nextcord


class Memes(commands.Cog):
	
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def memes(self,ctx,sub: typing.Optional[str] = "linuxmemes"):
        output = meme.get_meme(sub)
        try:
            for i in range(len(output)):
                await ctx.channel.send(file=nextcord.File(output[i]))
        except:
            await ctx.send('Oof something went wrong... Try changing subreddit')

    @commands.command()
    async def setmemesnum(self,ctx,num: typing.Optional[int] = 2):
        os.system("rm -f memes/number.txt")
        open('memes/number.txt', 'w').write(str(num))
        await ctx.reply("Memes number is now " + num)

    @commands.command()
    @commands.has_any_role('Owner', 'Admin')
    async def clearmemes(self,ctx):
        shutil.rmtree('memes/meme-folder/')
        os.system('mkdir memes/memes.txt')
        os.makedirs('memes/meme-folder/')
        open('memes/memes.txt', 'w')


def setup(bot):
    bot.add_cog(Memes(bot))
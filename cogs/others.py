from nextcord.ext import commands
from Assets.python.echo import echo
import typing
import nextcord
import random
import os

class Others(commands.Cog):
	
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount: typing.Optional[int]):
        bot = self.bot
        if amount == None:
            await ctx.channel.purge()
        else:
            await ctx.channel.purge(limit=amount + 1)

    @commands.command()
    @commands.has_any_role('Owner', 'Moderator', 'Admin')
    async def log(self, ctx):
        bot = self.bot
        echo("Showing System Log!")
        os.system("sudo rm -f Assets/Admin/log.sys")
        os.system("sudo systemctl status parrotbot.discord.service > Assets/Admin/log.sys")
        await ctx.reply(open('Assets/Admin/log.sys', 'r').read())
        os.system("sudo rm -f Assets/Admin/log.sys")

    @commands.command()
    @commands.has_any_role('Owner', 'Moderator', 'Admin')
    async def editstatus(self, ctx, *, status):
        bot = self.bot
        await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name=status))

    @commands.command()
    @commands.has_any_role('Owner', 'Admin', 'Moderator')
    async def DM(self, ctx, user: nextcord.User, *, message=None):
        bot = self.bot
        message = message or "This Message is sent via DM"
        await user.send(message)

    @commands.command()
    async def neofetch(self, ctx):
        bot = self.bot
        if ctx.author == bot.user:
            return
        if ctx.author.bot: return


        embed=nextcord.Embed(title="Neofetch:", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
        embed.add_field(name="Distro", value="Manjaro Linux", inline=False)
        embed.add_field(name="APU", value="Potato gen 6", inline=False)
        embed.add_field(name="RAM", value="4gb", inline=False)
        embed.set_image(url='https://i.ytimg.com/vi/caBFyIyDZME/hqdefault.jpg')
        await ctx.send(embed=embed)

    @commands.command()
    async def testurl(self, ctx, url):
        bot = self.bot
        os.system('rm Assets/Admin/url.txt.bak')
        os.system('cp Assets/Admin/url.txt Assets/Admin/url.txt.bak')
        old = open('Assets/Admin/url.txt', 'r').read()
        open('Assets/Admin/url.txt', 'w').write(old + "\n" + url)
        cmd = "curl " + url + " > Assets/Admin/curl.txt"
        os.system(cmd)
        await ctx.reply(open('Assets/Admin/curl.txt', 'r').read())
        os.system('rm Assets/Admin/curl.txt')




def setup(bot):
    bot.add_cog(Others(bot))
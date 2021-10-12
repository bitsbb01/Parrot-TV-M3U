from nextcord.ext import commands
from Assets.python.echo import echo
import typing
import nextcord
import os


class Autoupdate(commands.Cog):
	
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role('Owner', 'Admin')
    async def AAcontrol(self, ctx, args):
        if str(args) == "1" or str(args) == "start":
            await ctx.reply('Restarting BOT!')
            echo("Starting Aut-Update BOT!")
            os.system("sudo systemctl start parrotbot.service")
        if str(args) == "2" or str(args) == "restart":
            await ctx.reply('Restarting BOT!')
            echo("Restarting Aut-Update BOT!")
            os.system("sudo systemctl restart parrotbot.service")

        if str(args) == "3" or str(args) == "status":
            echo("Showing Auto-Update Log!")
            os.system("sudo rm -f Assets/Admin/log.sys")
            os.system("sudo systemctl status parrotbot.service > Assets/Admin/log-auto.sys")
            await ctx.reply(open('Assets/Admin/log-auto.sys', 'r').read())
            os.system("sudo rm -f Assets/Admin/log-auto.sys")


def setup(bot):
    bot.add_cog(Autoupdate(bot))
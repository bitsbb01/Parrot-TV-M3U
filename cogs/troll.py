from nextcord.ext import commands
import typing
import nextcord


class Troll(commands.Cog):
	
    def __init__(self, bot):
        self.bot = bot

@commands.command()
@commands.has_role('Owner')
async def spam(ctx, user: typing.Optional[str], times: typing.Optional[int] = 10, reason: typing.Optional[str] = "you're being spammed!"):
    for i in range(int(times)):
        await ctx.send(user + " " + reason)

@commands.command()
@commands.has_permissions(manage_messages = True)
async def sayasbot(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)



def setup(bot):
    bot.add_cog(Troll(bot))
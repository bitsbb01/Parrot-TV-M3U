from nextcord.ext import commands
import typing
import nextcord


class Kick(commands.Cog):
	
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user: typing.Optional[nextcord.Member], reason: typing.Optional[str] = "U got fucking yeeted"):
        bot = self.bot

        if ctx.author == bot.user:
            return
        if ctx.author.bot: return

        if user == None:
            embed=nextcord.Embed(title="Who do u want me to kick?:", color=0xff4c4c)
            embed.set_image(url='https://c.tenor.com/O_xuLx_lC-gAAAAC/stickman-smile.gif')
            await ctx.send(embed=embed)
        else:
            channel = bot.get_channel(896802105229201419)
            titleC = "Kicked " + str(user) + "!"
            embed=nextcord.Embed(title=titleC, color=0xff4c4c)
            embed.set_image(url='https://c.tenor.com/O_xuLx_lC-gAAAAC/stickman-smile.gif')
            if reason == "U got fucking yeeted":
                titleC2 = "Kicked " + str(user) + " by " + str(ctx.author)
            else:
                titleC2 = "Kicked " + str(user) + " by " + str(ctx.author) + " cuz " + reason
            embed2=nextcord.Embed(title=titleC2, color=0xff4c4c)
            embed2.set_image(url='https://c.tenor.com/O_xuLx_lC-gAAAAC/stickman-smile.gif')
            await ctx.send(embed=embed)
            await channel.send(embed=embed2)
            await ctx.guild.kick(user, reason=reason)


def setup(bot):
    bot.add_cog(Kick(bot))
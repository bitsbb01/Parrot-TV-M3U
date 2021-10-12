from nextcord.ext import commands
import typing
import nextcord


class Mute(commands.Cog):
	
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, user: typing.Optional[nextcord.Member]):
        mutedRole = nextcord.utils.get(ctx.guild.roles, name="Muted")
        mutedRole2 = nextcord.utils.get(ctx.guild.roles, name="Member")
        if user == None:
            embed=nextcord.Embed(title="Who should be silenced?", color=0xff4c4c)
            embed.set_image(url='https://c.tenor.com/RLuR6aGNAGEAAAAC/scpl-maszkos.gif')
            await ctx.send(embed=embed)
        else:
            titleC = "Silence has raised for " + str(user) + "!"
            embed=nextcord.Embed(title=titleC, color=0xff4c4c)
            embed.set_image(url='https://c.tenor.com/RLuR6aGNAGEAAAAC/scpl-maszkos.gif')
            await ctx.send(embed=embed)
            await user.add_roles(mutedRole)
            await user.remove_roles(mutedRole2)


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, user: typing.Optional[nextcord.Member]):
        mutedRole = nextcord.utils.get(ctx.guild.roles, name="Muted")
        mutedRole2 = nextcord.utils.get(ctx.guild.roles, name="Member")
        if user == None:
            embed=nextcord.Embed(title="Who should be unmuted?:", color=0x76ee00)
            embed.set_image(url='https://c.tenor.com/sikzoqOWHJ8AAAAM/unmute-me-unmute.gif')
            await ctx.send(embed=embed)
        else:
            titleC = "Silence has left for " + str(user) + "!"
            embed=nextcord.Embed(title=titleC, color=0x76ee00)
            embed.set_image(url='https://c.tenor.com/I62xyZQjD_sAAAAd/im-unmuted.gif')
            await ctx.send(embed=embed)
            await user.remove_roles(mutedRole)
            await user.add_roles(mutedRole2)


def setup(bot):
    bot.add_cog(Mute(bot))
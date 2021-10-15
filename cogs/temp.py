from nextcord.ext import commands
import typing
import nextcord
import asyncio


class Temp(commands.Cog):
	
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def tempmute(self, ctx, user: nextcord.Member, time: int):
        timemute = time * 60
        titleC = "Silence has raised for " + str(user) + " for " + str(time) + " mins" + "!"
        mutedRole = nextcord.utils.get(ctx.guild.roles, name="Muted")
        mutedRole2 = nextcord.utils.get(ctx.guild.roles, name="Member")    
        embed=nextcord.Embed(title=titleC, color=0xff4c4c)
        embed.set_image(url='https://c.tenor.com/RLuR6aGNAGEAAAAC/scpl-maszkos.gif')
        await ctx.send(embed=embed)
        await user.add_roles(mutedRole)
        await user.remove_roles(mutedRole2)
        await asyncio.sleep(timemute)
        await user.remove_roles(mutedRole)
        await user.add_roles(mutedRole2)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def tempban(self, ctx, user: nextcord.Member, time: int, reason: typing.Optional[str]):
        bot = self.bot
        timeban = time * 60
        channel = bot.get_channel(896798066848444466)
        titleC = "Killed " + str(user) + " for " + time + "!"
        embed=nextcord.Embed(title=titleC, color=0xff4c4c)
        embed.set_image(url='https://i.imgur.com/RkIfjMP.gif')
        titleC2 = "Killed " + str(user) + " for " + time + " by " + str(ctx.author)
        embed2=nextcord.Embed(title=titleC2, color=0xff4c4c)
        embed2.set_image(url='https://i.imgur.com/RkIfjMP.gif')
        titleC3 = "Revived " + str(user) + "!"
        embed3=nextcord.Embed(title=titleC3, color=0xff4c4c)
        embed3.set_image(url='https://c.tenor.com/KLMY48otv4gAAAAC/quantum-society-unbanned.gif')
        await ctx.send(embed=embed)
        await channel.send(embed=embed2)
        await ctx.guild.ban(user, reason=reason)
        await asyncio.sleep(timeban)
        await ctx.guild.unban(user)
        await channel.send(embed=embed3)
        await ctx.send(embed=embed3)




def setup(bot):
    bot.add_cog(Temp(bot))
from replit import db
from nextcord.ext import commands
import typing
import nextcord


class Warn(commands.Cog):
	
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, user: typing.Optional[nextcord.Member], reason):
        bot = self.bot
        channel = bot.get_channel(896791800830894121)
        us = str(user)
        warnnum = "None"
        channel = bot.get_channel(896798066848444466)
        titleC = "Killed " + str(user) + "!"
        embed=nextcord.Embed(title=titleC, color=0xff4c4c)
        embed.set_image(url='https://i.imgur.com/RkIfjMP.gif')
        titleC2 = "Killed " + str(user) + " by " + str(ctx.author)
        embed2=nextcord.Embed(title=titleC2, color=0xff4c4c)
        embed2.set_image(url='https://i.imgur.com/RkIfjMP.gif')
        str(us)
        if str(us) in db.keys():
          db[us] += 1
          if db[us] == 1:
            warnnum = "First"
          elif db[us] == 2:
            warnnum = "Second"
          elif db[us] == 3:
            warnnum = "Third"
            await ctx.send(embed=embed)
            await channel.send(embed=embed2)
            await ctx.guild.ban(user, reason="I thought 3 warn were enough. Looks like I was wrong!")
            del db[us]
        else:
          db[us] = 1

        line1 = str(user) + " has been warned for " + str(reason) + "!" + " This is his/her " + warnnum + " warning!"
        line2 = "Warned by " + str(ctx.author)
        embed=nextcord.Embed(title="Warn:", color=0xff4c4c) 
        embed.set_thumbnail(url="https://openclipart.org/image/2400px/svg_to_png/1695/zeimusu-Warning-sign.png")
        embed.add_field(name=line1, value=line2, inline=False)
        await ctx.send(embed=embed)
        await channel.send(embed=embed)






def setup(bot):
    bot.add_cog(Warn(bot))
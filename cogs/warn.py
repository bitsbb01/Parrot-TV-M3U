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
        line1 = str(user) + " has been warned for " + str(reason) + "!"
        line2 = "Warned by " + str(ctx.author)
        embed=nextcord.Embed(title="Warn:", color=0xff4c4c) 
        embed.set_thumbnail(url="https://openclipart.org/image/2400px/svg_to_png/1695/zeimusu-Warning-sign.png")
        embed.add_field(name=line1, value=line2, inline=False)
        await ctx.send(embed=embed)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Warn(bot))
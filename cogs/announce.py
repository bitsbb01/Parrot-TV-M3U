from nextcord.ext import commands
import typing
import nextcord
import os


class Announce(commands.Cog):
	
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role("Owner", "Admin")
    async def announce(self, ctx, channel:nextcord.TextChannel, title, msg, icon: typing.Optional[str] = "https://ParrotTV.github.io/Images/Favicon/favicon.png"):
        bot = self.bot
        await ctx.message.delete()
        from Assets.color import color
        embed=nextcord.Embed(title=str(title), color=color)
        embed.set_thumbnail(url=icon)
        embed.add_field(name=str(msg), value=str("Announced by ") + str(self, ctx.author), inline=False)
        await channel.send(embed=embed)
        await channel.send("@here")

    @commands.command()
    @commands.has_any_role("Owner", "Admin")
    async def announce2(self, ctx, channel:nextcord.TextChannel, title, msg, msg2, icon: typing.Optional[str] = "https://ParrotTV.github.io/Images/Favicon/favicon.png"):
        bot = self.bot
        await ctx.message.delete()
        from Assets.color import color
        embed=nextcord.Embed(title=str(title), color=color)
        embed.set_thumbnail(url=icon)
        embed.add_field(name=str(msg), value=str("--------------"), inline=False)
        embed.add_field(name=str(msg2), value=str("Announced by ") + str(self, ctx.author), inline=False)
        await channel.send(embed=embed)
        await channel.send("@here")

    @commands.command()
    @commands.has_any_role("Owner", "Admin")
    async def announce3(self, ctx, channel:nextcord.TextChannel, title, msg, msg2, msg3, icon: typing.Optional[str] = "https://ParrotTV.github.io/Images/Favicon/favicon.png"):
        bot = self.bot
        await ctx.message.delete()
        from Assets.color import color
        embed=nextcord.Embed(title=str(title), color=color)
        embed.set_thumbnail(url=icon)
        embed.add_field(name=str(msg), value=str("--------------"), inline=False)
        embed.add_field(name=str(msg2), value=str("--------------"), inline=False)
        embed.add_field(name=str(msg3), value=str("Announced by ") + str(self, ctx.author), inline=False)
        await channel.send(embed=embed)
        await channel.send("@here")

    @commands.command()
    @commands.has_any_role("Owner", "Admin")
    async def sac(ctx, color):
        if color == "default":
            colr = "0xA1BCD0"
        else:
            colr = color.replace("#", "0x")
        if os.path.exists('Assets/color.py'):
            os.remove('Assets/color.py')
        os.system("echo > Assets/color.py")
        with open('Assets/color.py', 'w') as f:
            line = "color=" + colr
            f.write(line)
            f.close()

        if color == "default":
            await ctx.reply("Default color is back!")
        else:
            await ctx.reply(color + " Is new color")

def setup(bot):
    bot.add_cog(Announce(bot))
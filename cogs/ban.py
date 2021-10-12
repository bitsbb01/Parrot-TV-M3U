from nextcord.ext import commands
import typing
import nextcord


class Ban(commands.Cog):
	
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user: typing.Optional[nextcord.Member], reason: typing.Optional[str] = "U got fucking yeeted"):
        bot = self.bot

        if user == None:
            embed=nextcord.Embed(title="Who do u want me to kill?:", color=0xff4c4c)
            embed.set_image(url='https://i.imgur.com/RkIfjMP.gif')
            await ctx.send(embed=embed)
        else:
            channel = bot.get_channel(896798066848444466)
            titleC = "Killed " + str(user) + "!"
            embed=nextcord.Embed(title=titleC, color=0xff4c4c)
            embed.set_image(url='https://i.imgur.com/RkIfjMP.gif')
            titleC2 = "Killed " + str(user) + " by " + str(ctx.author)
            embed2=nextcord.Embed(title=titleC2, color=0xff4c4c)
            embed2.set_image(url='https://i.imgur.com/RkIfjMP.gif')
            await ctx.send(embed=embed)
            await channel.send(embed=embed2)
            await ctx.guild.ban(user, reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, user: typing.Optional[str]):
        bot = self.bot

        if ctx.author == bot.user:
            return
        if ctx.author.bot: return

        if user == None:
            embed=nextcord.Embed(title="Who do u want me to revive?:", color=0x76ee00)
            embed.set_image(url='https://c.tenor.com/4sYpvIJeA_kAAAAM/kogama-tokeeto-banwave-kogama.gif')
            await ctx.send(embed=embed)
        else:
            banned_users = await ctx.guild.bans()
            
            member_name, member_discriminator = user.split('#')
            for ban_entry in banned_users:
                user = ban_entry.user
                
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    channel = bot.get_channel(896798066848444466)
                    embed=nextcord.Embed(title="Revived " + str(user) + "!", color=0x76ee00)
                    embed.set_image(url='https://c.tenor.com/KLMY48otv4gAAAAC/quantum-society-unbanned.gif')
                    embed2=nextcord.Embed(title="Revived " + str(user) + " by " + str(ctx.author), color=0x76ee00)
                    embed2.set_image(url='https://c.tenor.com/KLMY48otv4gAAAAC/quantum-society-unbanned.gif')
                    await ctx.send(embed=embed)
                    await channel.send(embed=embed2)


def setup(bot):
    bot.add_cog(Ban(bot))
from nextcord.ext import commands
import random
import nextcord


class Send(commands.Cog):
	
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sendrules(self, ctx):
        bot = self.bot
        await ctx.message.delete()

        embed=nextcord.Embed(title="Rules:", color=0xbf0000)
        embed.add_field(name="-----------------------", value="1. No Spam or flooding the chat with messages. Do not type in ALL CAPS.", inline=False)
        embed.add_field(name="-----------------------", value="2. No bashing or heated arguments to other people in the chat.", inline=False)
        embed.add_field(name="-----------------------", value="3. No adult (18+), explicit, or controversial messages.", inline=False)
        embed.add_field(name="-----------------------", value="4. No racism or degrading content.", inline=False)
        embed.add_field(name="-----------------------", value="5. No excessive cursing.", inline=False)
        embed.add_field(name="-----------------------", value="6. No advertising  (Only with Permission).", inline=False)
        embed.add_field(name="-----------------------", value="7. No referral links (Only with Permission).", inline=False)
        embed.add_field(name="-----------------------", value="8. No offensive names.", inline=False)
        embed.add_field(name="-----------------------", value="9. Do not argue with staff. Decisions are final.", inline=False)
        await ctx.send(embed=embed)


    @commands.command()
    async def sendkodi(self, ctx):
        bot = self.bot

        await ctx.message.delete()


        embed=nextcord.Embed(title="KODI:", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
        embed.set_thumbnail(url="https://ParrotTV.github.io/Images/Favicon/favicon.png")
        embed.add_field(name="Repository:", value="```https://bit.ly/3zYeTc7```", inline=False)
        embed.add_field(name="KODI 19.0:", value="```https://bit.ly/2WhlL5B```", inline=False)
        embed.add_field(name="KODI 18.9:", value="```https://bit.ly/3mpY1a0```", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def sendweb(self, ctx):
        bot = self.bot
        await ctx.message.delete()


        embed=nextcord.Embed(title="Websites:", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
        embed.set_thumbnail(url="https://ParrotTV.github.io/Images/Favicon/favicon.png")
        embed.add_field(name="URL 1:", value="```https://ParrotTV.github.io```", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def sendm3u(self, ctx):
        bot = self.bot
        await ctx.message.delete()


        embed=nextcord.Embed(title="M3U Links:", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
        embed.set_thumbnail(url="https://ParrotTV.github.io/Images/Favicon/favicon.png")
        embed.add_field(name="World Wide:", value="```https://bit.ly/PPM3U```", inline=False)
        embed.add_field(name="English only:", value="```https://bit.ly/PPM3U-E```", inline=False)
        embed.add_field(name="Czechoslovak:", value="```https://bit.ly/PPM3U-CS```", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def sendepg(self, ctx):
        bot = self.bot
        await ctx.message.delete()


        embed=nextcord.Embed(title="EPG Links:", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
        embed.set_thumbnail(url="https://ParrotTV.github.io/Images/Favicon/favicon.png")
        embed.add_field(name="CZ / SK:", value="```https://bit.ly/PPEPG4```", inline=False)
        embed.add_field(name="US:", value="```https://iptv-org.github.io/epg/guides/tvtv.us.guide.xml```", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Send(bot))
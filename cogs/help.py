from nextcord.ext import commands
import typing
import random
import nextcord


class Help(commands.Cog):
	
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, page: typing.Optional[str] = "0"):
        bot = self.bot

        if page == "0":
            embedh=nextcord.Embed(title="User Commands:", description="It Looks Like u Need Help :flushed:!", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
            embedh.add_field(name="=======================", value="```p!help``` - Show this page!", inline=False)
            embedh.add_field(name="=======================", value="```p!help user``` - Show user commands!", inline=False)
            embedh.add_field(name="=======================", value="```p!help mod``` - Show mod commands!", inline=False)
            embedh.add_field(name="=======================", value="```p!help admin``` - Show admin commands!", inline=False)
            embedh.add_field(name="=======================", value="```p!help owner``` - Show owner commands!", inline=False)
            await ctx.send(embed=embedh)
        elif page == "user":
            embed=nextcord.Embed(title="User Commands:", description="It Looks Like u Need Help :flushed:!", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
            embed.add_field(name="=======================", value="```p!src``` - Show Source Code!", inline=False)
            embed.add_field(name="=======================", value="```p!neofetch``` - Show system info!", inline=False)
            await ctx.send(embed=embed)
        elif page == "mod":
            embed2=nextcord.Embed(title="Mod Commands:", description="It Looks Like u Need Help :flushed:!", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
            embed2.add_field(name="=======================", value="```p!log``` - Show System Service Log!", inline=False)
            embed2.add_field(name="=======================", value="```p!kick [user] [reason - not required]``` - Kick's People!", inline=False)
            embed2.add_field(name="=======================", value="```p!mute [user]``` - Mutes's People!", inline=False)
            embed2.add_field(name="=======================", value="```p!warn [user] [reason]``` - Warn's People!", inline=False)
            embed2.add_field(name="=======================", value="```p!unmute [user]``` - Unmute's People!", inline=False)
            embed2.add_field(name="=======================", value="```p!clear [number]``` - Clear [number] messages!", inline=False)
            await ctx.send(embed=embed2)
        elif page == "admin":
            embed3=nextcord.Embed(title="Admin Commands:", description="It Looks Like u Need Help :flushed:!", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
            embed3.add_field(name="=======================", value="```p!AAcontrol [start/restart/status]``` - Auto-Update service control!", inline=False)
            embed3.add_field(name="=======================", value="```p!announce [room] [title] [message] [icon - not required]``` - Auto-Update service control!", inline=False)
            embed3.add_field(name="=======================", value="```p!announce2 [room] [title] [message] [message - second row] [icon - not required]``` - Auto-Update service control!", inline=False)
            embed3.add_field(name="=======================", value="```p!announce3 [room] [title] [message] [message - second row] [message - third row] [icon - not required]``` - Auto-Update service control!", inline=False)
            embed3.add_field(name="=======================", value="```p!ban [user] [reason - not required]``` - Ban's People!", inline=False)
            embed3.add_field(name="=======================", value="```p!unban [username#tag]``` - Unban's people!", inline=False)
            embed3.add_field(name="=======================", value="```p!sac [hex color / default]``` - Change p!announce command color!", inline=False)
            await ctx.send(embed=embed3)
        elif page == "owner":
            embed4=nextcord.Embed(title="Owner Commands:", description="It Looks Like u Need Help :flushed:!", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
            embed4.add_field(name="=======================", value="```p!sendrules``` - Send rules.", inline=False)
            embed4.add_field(name="=======================", value="```p!sendweb``` - Send website domains.", inline=False)
            embed4.add_field(name="=======================", value="```p!sendkodi``` - Send KODI Links.", inline=False)
            embed4.add_field(name="=======================", value="```p!sendepg``` - Send EPG URLs.", inline=False)
            embed4.add_field(name="=======================", value="```p!sendm3u``` - Send M3U URLs.", inline=False)
            await ctx.send(embed=embed4)


def setup(bot):
    bot.add_cog(Help(bot))
from replit import db
from nextcord.ext import commands
import typing
import nextcord


class DB(commands.Cog):
	
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role('Owner')
    async def cleardb(self, ctx):
      i = 0
      for key in db.keys():
        del db[key]
        i =+ 1
      await ctx.reply("Cleared " + str(i) + " keys!")

    @commands.command()
    @commands.has_role('Owner')
    async def listdb(self, ctx):
      ctx.reply(db.keys())





def setup(bot):
    bot.add_cog(DB(bot))
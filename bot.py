import os
import nextcord
from nextcord.ext import commands
from Auth.auth import disToken

bot = commands.Bot(command_prefix=('p!', '-'), help_command=None)

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name="-help"))


@bot.command()
@commands.has_role('Owner')
async def load(ctx, extension):
	bot.load_extension(f'cogs.{extension}')
	await ctx.send("Loaded " + extension)

@bot.command()
@commands.has_role('Owner')
async def unload(ctx, extension):
	bot.unload_extension(f'cogs.{extension}')
	await ctx.send("Unoaded " + extension)

@bot.command()
@commands.has_role('Owner')
async def reload(ctx, extension):
	bot.unload_extension(f'cogs.{extension}')
	bot.load_extension(f'cogs.{extension}')
	await ctx.send("Reloaded " + extension)

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(disToken)
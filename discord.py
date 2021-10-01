from nextcord import guild
from nextcord.ext import commands
from typing import List
import nextcord
import typing
import random
from Auth.auth import disToken
from make import RemoveMode1, RemoveMode2, Clear, getUSTVGO, replaceUStVicons, updateEPG, tar, MakeCS, MakeEng, MakeMain, Git, pushbulletMode

bot = commands.Bot(command_prefix='!')

@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)



@bot.command()
async def ban(ctx, members: commands.Greedy[nextcord.Member],
                   delete_days: typing.Optional[int] = 0, *,
                   reason: str):
    for member in members:
        await member.ban(delete_message_days=delete_days, reason=reason)

@bot.command()
async def uid(ctx):
    await ctx.send(guild.client.id)


bot.run(disToken)
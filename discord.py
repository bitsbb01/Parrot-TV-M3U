from nextcord import client, guild
from nextcord.ext import commands
from typing import List
import nextcord
import typing
import random
import os
from Auth.auth import disToken
from make import RemoveMode1, RemoveMode2, Clear, getUSTVGO, replaceUStVicons, updateEPG, tar, MakeCS, MakeEng, MakeMain, Git, pushbulletMode



def echo(msg):
    echocmd = "sudo echo " + '"' + msg + '"'
    os.system(echocmd)

def Mode2():
    RemoveMode2()
    getUSTVGO()
    replaceUStVicons()
    MakeCS()
    MakeEng()
    MakeMain()
    Git()
    pushbulletMode(2)


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def M3U(ctx):
    await ctx.reply('OK!', mention_author=True)
    echo("Running M3U Update!")
    Mode2()
    await ctx.reply("Done! - without EPG!", mention_author=True)


@bot.command()
async def ban(ctx, members: commands.Greedy[nextcord.Member],
                   delete_days: typing.Optional[int] = 0, *,
                   reason: str):
    for member in members:
        await member.ban(delete_message_days=delete_days, reason=reason)


@bot.command()
@commands.has_permissions(manage_roles=True)
async def giverole(ctx, user: nextcord.Member=None, rolename:nextcord.Role="Owner"):
    if rolename in user.roles:
        await ctx.send("Person already has role")
    else:
        await ctx.send("Person doesn't have the role")



bot.run(disToken)
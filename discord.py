from nextcord import client, guild
from nextcord.ext import commands
from typing import List
import nextcord
import time
import typing
import random
import os
from nextcord.message import Message
from Auth.auth import disToken
from make import RemoveMode2, getUSTVGO, replaceUStVicons, MakeCS, MakeEng, MakeMain, Git, pushbulletMode, remPYC, Clear

def RemoveMode1():
    if os.path.exists("Czechoslovaia.m3u"):
        os.remove("Czechoslovaia.m3u")

    if os.path.exists("English.m3u"):
        os.remove("English.m3u")

    if os.path.exists("Main.m3u"):
        os.remove("Main.m3u")

    if os.path.exists("EPG/ustvgo_epg.xml"):
        os.remove("EPG/ustvgo_epg.xml")

    if os.path.exists("Assets/Channels/ustvgo.m3u"):
        os.remove("Assets/Channels/ustvgo.m3u")

    if os.path.exists("Assets/USTVGOreplace/data.txt"):
        os.remove("Assets/USTVGOreplace/data.txt")

    if os.path.exists("EPG/tvtv.us.guide.xml"):
        os.remove("EPG/tvtv.us.guide.xml")

    if os.path.exists("EPG/tvtv.us.guide.xml.1"):
        os.remove("EPG/tvtv.us.guide.xml.1")

    if os.path.exists("EPG/CZ.xml"):
        os.remove("EPG/CZ.xml")
        
    if os.path.exists("EPG/CZ.xml"):
        os.remove("EPG/EPG.xml")

    if os.path.exists("EPG/EPG.tar.gz"):
        os.remove("EPG/EPG.tar.gz")

    if os.path.exists("EPG/EPG.xml"):
        os.remove("EPG/EPG.xml")

def echo(msg):
    echocmd = "sudo echo " + '"' + msg + '"'
    os.system(echocmd)

def tar():
    os.system("cp EPG/EPG.xml EPG.xml")
    os.system("tar -czvf EPG.tar.gz EPG.xml")
    os.system("mv EPG.tar.gz EPG/")
    if os.path.exists("EPG.xml"):
        os.remove("EPG.xml")

def updateEPG():
    os.system("sudo python3 EPG/Generator/generator.py")

def Mode1():
    RemoveMode1()
    Clear()
    getUSTVGO()
    replaceUStVicons()
    updateEPG()
    tar()
    MakeCS()
    MakeEng()
    MakeMain()
    Git()
    pushbulletMode(1)
    remPYC()

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
    echo("------------------")
    echo(str(bot.user.name) + " has connected to Discord!")
    echo("------------------")

@bot.command()
async def M3U(ctx):
    await ctx.reply('OK!', mention_author=True)
    echo("Running M3U Update!")
    Mode2()
    await ctx.reply("Done! - without EPG!", mention_author=True)

@bot.command()
@commands.has_role('Owner')
async def M3UEPG(ctx):
    await ctx.reply('OK!', mention_author=True)
    echo("Running M3U and EPG Update!")
    Mode1()
    await ctx.reply("Done! - with EPG!", mention_author=True)

@bot.command()
@commands.has_role('Owner')
async def ban(ctx, members: commands.Greedy[nextcord.Member],
                   delete_days: typing.Optional[int] = 0, *,
                   reason: str):
    for member in members:
        await member.ban(delete_message_days=delete_days, reason=reason)
        await ctx.send(member + " was banned for " + delete_days + " cuz he: " + reason)

@bot.command()
@commands.has_role('Owner')
async def log(ctx):
    echo("Showing System Log!")
    os.system("sudo rm -f Assets/Admin/log.sys")
    os.system("sudo systemctl status parrotbot.discord.service > Assets/Admin/log.sys")
    await ctx.reply(open('Assets/Admin/log.sys', 'r').read())
    os.system("sudo rm -f Assets/Admin/log.sys")

@bot.command()
@commands.has_role('Owner')
async def resetbot(ctx):
    await ctx.reply('Restarting BOT!')
    echo("Restarting BOT:")
    os.system("sudo systemctl restart parrotbot.discord.service")

@bot.command()
async def rempyc(ctx):
    echo("Removing PYC")
    remPYC()
    await ctx.reply("Done!")

@bot.command()
@commands.has_role('Owner')
async def stt(ctx, args):
    if os.path.exists("Assets/Service/timeou.txt"):
        os.system('sudo rm -f Assets/Service/timeou.txt')
    timeouttime = str(args)
    open('Assets/Service/timeou.txt', 'w').write(timeouttime)
    await ctx.reply("New auto-update timeout is now: " + timeouttime)

@bot.command()
@commands.has_role('Owner')
async def AAcontrol(ctx, args):
    if str(args) == "1" or str(args) == "start":
        await ctx.reply('Restarting BOT!')
        echo("Starting Aut-Update BOT!")
        os.system("sudo systemctl start parrotbot.service")
    if str(args) == "2" or str(args) == "restart":
        await ctx.reply('Restarting BOT!')
        echo("Restarting Aut-Update BOT!")
        os.system("sudo systemctl restart parrotbot.service")
    if str(args) == "3" or str(args) == "stop":
        await ctx.reply('Restarting BOT!')
        echo("Stopping Aut-Update BOT!:")
        os.system("sudo systemctl stop parrotbot.service")
    if str(args) == "4" or str(args) == "status":
        echo("Showing Auto-Update Log!")
        os.system("sudo rm -f Assets/Admin/log.sys")
        os.system("sudo systemctl status parrotbot.service > Assets/Admin/log-auto.sys")
        await ctx.reply(open('Assets/Admin/log-auto.sys', 'r').read())
        os.system("sudo rm -f Assets/Admin/log-auto.sys")

@bot.command()
async def neofetch(ctx):
    if ctx.author == bot.user:
        return
    if ctx.author.bot: return


    embed=nextcord.Embed(title="Neofetch:", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
    embed.add_field(name="Distro", value="Manjaro Linux", inline=False)
    embed.add_field(name="APU", value="Potato gen 6", inline=False)
    embed.add_field(name="RAM", value="4gb", inline=False)
    embed.set_image(url='https://i.ytimg.com/vi/caBFyIyDZME/hqdefault.jpg')
    await ctx.send(embed=embed)

@bot.command()
@commands.help()
async def help(ctx):
    embed=nextcord.Embed(title="Neofetch:", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
    embed.add_field(name="Distro", value="Manjaro Linux", inline=False)
    embed.add_field(name="APU", value="Potato gen 6", inline=False)
    embed.add_field(name="RAM", value="4gb", inline=False)
    embed.set_image(url='https://i.ytimg.com/vi/caBFyIyDZME/hqdefault.jpg')
    await ctx.send(embed=embed)

bot.run(disToken)
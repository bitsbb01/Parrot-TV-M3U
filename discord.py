from nextcord import client, guild
from nextcord.ext import commands
from typing import List
import nextcord
import typing
import random
import os
from nextcord.message import Message
from Auth.auth import disToken
from make import RemoveMode2, getUSTVGO, replaceUStVicons, MakeCS, MakeEng, MakeMain, Git, pushbulletMode, remPYC, Clear

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
    Clear()
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
async def embed(ctx):
    randnum = random.randint(1, 10)
    if str(randnum) == "1":
        clrEmbed=0x08ff00
    if str(randnum) == "2":
        clrEmbed=0x00ffff
    if str(randnum) == "3":
        clrEmbed=0xfa6900
    if str(randnum) == "4":
        clrEmbed=0xf98082
    if str(randnum) == "5":
        clrEmbed=0x75edeb
    if str(randnum) == "6":
        clrEmbed=0x3d85c6
    if str(randnum) == "7":
        clrEmbed=0x0b5394
    if str(randnum) == "8":
        clrEmbed=0xaa35c
    if str(randnum) == "9":
        clrEmbed=0x4fa875
    if str(randnum) == "10":
        clrEmbed=0x43765f

    embed=nextcord.Embed(title="Neofetch:", color=int(clrEmbed))
    embed.add_field(name="Distro", value="Manjaro Linux", inline=False)
    embed.add_field(name="APU", value="Potato gen 6", inline=False)
    embed.add_field(name="RAM", value="4gb", inline=False)
    embed.set_image(url='https://i.ytimg.com/vi/caBFyIyDZME/hqdefault.jpg')
    await ctx.send(embed=embed)

bot.run(disToken)
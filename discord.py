from nextcord import client, guild
from nextcord.ext import commands
from typing import List
import nextcord
import typing
import random
import os
from nextcord.message import Message
from Auth.auth import disToken
import os
from datetime import datetime
from Assets.python.time import tz
from make import RemoveMode2, getUSTVGO, replaceUStVicons, MakeCS, MakeEng, MakeMain, Git, remPYC, Clear
bot = commands.Bot(command_prefix='!', help_command=None)

now = datetime.now(tz)
time = now.strftime("%H:%M:%S")
 
def RemoveMode1():
    if os.path.exists("Czechoslovaia.m3u"):
        os.remove("Czechoslovaia.m3u")

    if os.path.exists("English.m3u"):
        os.remove("English.m3u")

    if os.path.exists("Main.m3u"):
        os.remove("Main.m3u")

    if os.path.exists("EPG/ustvgo_epg.xml"):
        os.remove("EPG/ustvgo_epg.xml")

    if os.path.exists("Assets/Channels/US/ustvgo.m3u"):
        os.remove("Assets/Channels/US/ustvgo.m3u")

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
    remPYC()

def Mode2():
    RemoveMode2()
    getUSTVGO()
    replaceUStVicons()
    MakeCS()
    MakeEng()
    MakeMain()
    Git()

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
@commands.has_any_role('Owner', 'Moderator', 'Admin')
async def M3UEPG(ctx):
    await ctx.reply('OK!', mention_author=True)
    echo("Running M3U and EPG Update!")
    Mode1()
    await ctx.reply("Done! - with EPG!", mention_author=True)

@bot.command()
async def code(ctx):
    await ctx.reply('https://github.com/ParrotDevelopers/Parrot-TV-M3U/')

"""
async def ban(ctx, members: commands.Greedy[nextcord.Member],
                   delete_days: typing.Optional[int] = 0, *,
                   reason: str):
    for member in members:
        await member.ban(delete_message_days=delete_days, reason=reason)
        await ctx.send(member + " was banned for " + delete_days + " cuz he: " + reason)

"""


@bot.command()
@commands.has_role('Owner')
async def ban(ctx, user: typing.Optional[nextcord.Member], reason: typing.Optional[str] = "U got fucking yeeted"):
    if ctx.author == bot.user:
        return
    if ctx.author.bot: return

    if user == None:
        embed=nextcord.Embed(title="Who do u want me to kill?:", color=0xff4c4c)
        embed.set_image(url='https://i.imgur.com/RkIfjMP.gif')
        await ctx.send(embed=embed)
    else:
        titleC = "Killed " + str(user) + "!"
        embed=nextcord.Embed(title=titleC, color=0xff4c4c)
        embed.set_image(url='https://i.imgur.com/RkIfjMP.gif')
        await ctx.send(embed=embed)
        await ctx.guild.ban(user, reason=reason)

@bot.command()
@commands.has_any_role('Owner', 'Moderator', 'Admin')
async def log(ctx):
    echo("Showing System Log!")
    os.system("sudo rm -f Assets/Admin/log.sys")
    os.system("sudo systemctl status parrotbot.discord.service > Assets/Admin/log.sys")
    await ctx.reply(open('Assets/Admin/log.sys', 'r').read())
    os.system("sudo rm -f Assets/Admin/log.sys")

@bot.command()
@commands.has_any_role('Owner', 'Moderator', 'Admin')
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
@commands.has_any_role('Owner', 'Admin')
async def stt(ctx, args):
    if os.path.exists("Assets/Service/timeou.txt"):
        os.system('sudo rm -f Assets/Service/timeou.txt')
    timeouttime = str(args)
    open('Assets/Service/timeou.txt', 'w').write(timeouttime)
    await ctx.reply("New auto-update timeout is now: " + timeouttime)

@bot.command()
@commands.has_any_role('Owner', 'Admin')
async def AAcontrol(ctx, args):
    if str(args) == "1" or str(args) == "start":
        await ctx.reply('Restarting BOT!')
        echo("Starting Aut-Update BOT!")
        os.system("sudo systemctl start parrotbot.service")
    if str(args) == "2" or str(args) == "restart":
        await ctx.reply('Restarting BOT!')
        echo("Restarting Aut-Update BOT!")
        os.system("sudo systemctl restart parrotbot.service")

    if str(args) == "3" or str(args) == "status":
        echo("Showing Auto-Update Log!")
        os.system("sudo rm -f Assets/Admin/log.sys")
        os.system("sudo systemctl status parrotbot.service > Assets/Admin/log-auto.sys")
        await ctx.reply(open('Assets/Admin/log-auto.sys', 'r').read())
        os.system("sudo rm -f Assets/Admin/log-auto.sys")


@bot.command()
@commands.has_role('Owner')
async def sendm3u(ctx):
    if ctx.author == bot.user:
        return
    if ctx.author.bot: return

    await ctx.message.delete()


    embed=nextcord.Embed(title="M3U Links:", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
    embed.set_thumbnail(url="https://parrottv.tk/Images/Favicon/favicon.png")
    embed.add_field(name="World Wide:", value="```https://bit.ly/PPM3U```", inline=False)
    embed.add_field(name="English only:", value="```https://bit.ly/PPM3U-E```", inline=False)
    embed.add_field(name="Czechoslovak:", value="```https://bit.ly/PPM3U-CS```", inline=False)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_role('Owner')
async def sendepg(ctx):
    if ctx.author == bot.user:
        return
    if ctx.author.bot: return

    await ctx.message.delete()


    embed=nextcord.Embed(title="EPG Links:", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
    embed.set_thumbnail(url="https://parrottv.tk/Images/Favicon/favicon.png")
    embed.add_field(name="CZ / SK:", value="```https://bit.ly/PPEPG3```", inline=False)
    embed.add_field(name="US:", value="```https://iptv-org.github.io/epg/guides/tvtv.us.guide.xml```", inline=False)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_role('Owner')
async def sendkodi(ctx):
    if ctx.author == bot.user:
        return
    if ctx.author.bot: return

    await ctx.message.delete()


    embed=nextcord.Embed(title="KODI:", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
    embed.set_thumbnail(url="https://parrottv.tk/Images/Favicon/favicon.png")
    embed.add_field(name="Repository:", value="```https://bit.ly/3zYeTc7```", inline=False)
    embed.add_field(name="KODI 19.0:", value="```https://bit.ly/2WhlL5B```", inline=False)
    embed.add_field(name="KODI 18.9:", value="```https://bit.ly/3mpY1a0```", inline=False)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_role('Owner')
async def sendweb(ctx):
    if ctx.author == bot.user:
        return
    if ctx.author.bot: return

    await ctx.message.delete()


    embed=nextcord.Embed(title="Websites:", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
    embed.set_thumbnail(url="https://parrottv.tk/Images/Favicon/favicon.png")
    embed.add_field(name="URL 1:", value="```https://parrottv.tk```", inline=False)
    embed.add_field(name="URL 2:", value="```https://ParrotTV.github.io```", inline=False)
    await ctx.send(embed=embed)



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
async def sendrules(ctx):
    if ctx.author == bot.user:
        return
    if ctx.author.bot: return

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


@bot.command()
async def help(ctx):
    if ctx.author == bot.user:
        return
    if ctx.author.bot: return


    embed=nextcord.Embed(title="Help:", description="It Looks Like u Need Help :flushed:!", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
    embed.add_field(name="=======================", value="```!M3U``` - Runs M3U Update Without EPG! [Admin not required]", inline=False)
    embed.add_field(name="=======================", value="```!M3UEPG``` - Runs M3U Update With EPG! [Mod required]", inline=False)
    embed.add_field(name="=======================", value="```!ban``` - Ban's People! [Owner only]", inline=False)
    embed.add_field(name="=======================", value="```!log``` - Show System Service Log! [Mod required]", inline=False)
    embed.add_field(name="=======================", value="```!resetbot``` - Restart Discord BOT! [Mod required]", inline=False)
    embed.add_field(name="=======================", value="```!rempyc``` - Remove pycahce! [Admin not required]", inline=False)
    embed.add_field(name="=======================", value="```!neofetch``` - Show system info! [Admin not required]", inline=False)
    embed.add_field(name="=======================", value="```!stt [time in seconds]``` - Set Auto-Update Timeout! [Admin required]", inline=False)
    embed.add_field(name="=======================", value="```!AAcontrol [start/restart/status]``` - Auto-Update service control! [Admin equired]", inline=False)
    await ctx.send(embed=embed)


bot.run(disToken)
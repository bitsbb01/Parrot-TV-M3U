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
from make import RemoveMode2, getUSTVGO, replaceUStVicons, MakeCS, MakeEng,MakePriv ,MakeMain, Git, remPYC, Clear
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

    if os.path.exists("Assets/Private/Private.m3u"):
        os.remove("Assets/Private/Private.m3u")

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
    MakePriv()
    Git()
    remPYC()

def Mode2():
    RemoveMode2()
    getUSTVGO()
    replaceUStVicons()
    MakeCS()
    MakeEng()
    MakeMain()
    MakePriv()
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
@commands.has_any_role("Owner", "Admin")
async def announce(ctx, channel:nextcord.TextChannel, title, msg, icon: typing.Optional[str] = "https://ParrotTV.github.io/Images/Favicon/favicon.png"):
    await ctx.message.delete()

    embed=nextcord.Embed(title=str(title), color=0xA1BCD0)
    embed.set_thumbnail(url=icon)
    embed.add_field(name=str(msg), value=str("Announced by ") + str(ctx.author), inline=False)
    await channel.send(embed=embed)
    await channel.send(ctx.message.guild.default_role)

@bot.command()
@commands.has_any_role("Owner", "Admin")
async def announce2(ctx, channel:nextcord.TextChannel, title, msg, msg2, icon: typing.Optional[str] = "https://ParrotTV.github.io/Images/Favicon/favicon.png"):
    await ctx.message.delete()

    embed=nextcord.Embed(title=str(title), color=0xA1BCD0)
    embed.set_thumbnail(url=icon)
    embed.add_field(name=str(msg), value=str("--------------"), inline=False)
    embed.add_field(name=str(msg2), value=str("Announced by ") + str(ctx.author), inline=False)
    await channel.send(embed=embed)
    await channel.send(ctx.message.guild.default_role)

@bot.command()
@commands.has_any_role("Owner", "Admin")
async def announce3(ctx, channel:nextcord.TextChannel, title, msg, msg2, msg3, icon: typing.Optional[str] = "https://ParrotTV.github.io/Images/Favicon/favicon.png"):
    await ctx.message.delete()

    embed=nextcord.Embed(title=str(title), color=0xA1BCD0)
    embed.set_thumbnail(url=icon)
    embed.add_field(name=str(msg), value=str("--------------"), inline=False)
    embed.add_field(name=str(msg2), value=str("--------------"), inline=False)
    embed.add_field(name=str(msg3), value=str("Announced by ") + str(ctx.author), inline=False)
    await channel.send(embed=embed)
    await channel.send(ctx.message.guild.default_role)

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

@bot.command()
async def src(ctx):
    await ctx.send("Parrot TV M3U Source Code:")
    await ctx.send("https://github.com/ParrotDevelopers/Parrot-TV-M3U/")

@bot.command()
@commands.has_permissions(ban_members = True)
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
    embed.set_thumbnail(url="https://ParrotTV.github.io/Images/Favicon/favicon.png")
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
    embed.set_thumbnail(url="https://ParrotTV.github.io/Images/Favicon/favicon.png")
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
    embed.set_thumbnail(url="https://ParrotTV.github.io/Images/Favicon/favicon.png")
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
    embed.set_thumbnail(url="https://ParrotTV.github.io/Images/Favicon/favicon.png")
    embed.add_field(name="URL 1:", value="```https://ParrotTV.github.io```", inline=False)
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
async def help(ctx, page: typing.Optional[str] = "0"):
    if ctx.author == bot.user:
        return
    if ctx.author.bot: return

    if page == "0":
        embedh=nextcord.Embed(title="User Commands:", description="It Looks Like u Need Help :flushed:!", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
        embedh.add_field(name="=======================", value="```!help``` - Show this page!", inline=False)
        embedh.add_field(name="=======================", value="```!help user``` - Show user commands!", inline=False)
        embedh.add_field(name="=======================", value="```!help mod``` - Show mod commands!", inline=False)
        embedh.add_field(name="=======================", value="```!help admin``` - Show admin commands!", inline=False)
        embedh.add_field(name="=======================", value="```!help owner``` - Show owner commands!", inline=False)
        await ctx.send(embed=embedh)
    elif page == "user":
        embed=nextcord.Embed(title="User Commands:", description="It Looks Like u Need Help :flushed:!", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
        embed.add_field(name="=======================", value="```!M3U``` - Runs M3U Update Without EPG!", inline=False)
        embed.add_field(name="=======================", value="```!src``` - Show Source Code!", inline=False)
        embed.add_field(name="=======================", value="```!rempyc``` - Remove pycahce!", inline=False)
        embed.add_field(name="=======================", value="```!neofetch``` - Show system info!", inline=False)
        await ctx.send(embed=embed)
    elif page == "mod":
        embed2=nextcord.Embed(title="Mod Commands:", description="It Looks Like u Need Help :flushed:!", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
        embed2.add_field(name="=======================", value="```!M3UEPG``` - Runs M3U Update With EPG!", inline=False)
        embed2.add_field(name="=======================", value="```!log``` - Show System Service Log!", inline=False)
        embed2.add_field(name="=======================", value="```!resetbot``` - Restart Discord BOT!", inline=False)
        await ctx.send(embed=embed2)
    elif page == "admin":
        embed3=nextcord.Embed(title="Admin Commands:", description="It Looks Like u Need Help :flushed:!", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
        embed3.add_field(name="=======================", value="```!stt [time in seconds]``` - Set Auto-Update Timeout!", inline=False)
        embed3.add_field(name="=======================", value="```!AAcontrol [start/restart/status]``` - Auto-Update service control!", inline=False)
        embed3.add_field(name="=======================", value="```!announce [room] [title] [message] [icon - not required]``` - Auto-Update service control!", inline=False)
        embed3.add_field(name="=======================", value="```!announce2 [room] [title] [message] [message - second row] [icon - not required]``` - Auto-Update service control!", inline=False)
        embed3.add_field(name="=======================", value="```!announce3 [room] [title] [message] [message - second row] [message - third row] [icon - not required]``` - Auto-Update service control!", inline=False)
        embed3.add_field(name="=======================", value="```!ban [user] [reason - not required]``` - Ban's People!", inline=False)
        await ctx.send(embed=embed3)
    elif page == "owner":
        embed4=nextcord.Embed(title="Owner Commands:", description="It Looks Like u Need Help :flushed:!", color=int(random.randint(0000, 9999)))  # int(clrEmbed)
        embed4.add_field(name="=======================", value="```!sendrules``` - Send rules.", inline=False)
        embed4.add_field(name="=======================", value="```!sendweb``` - Send website domains.", inline=False)
        embed4.add_field(name="=======================", value="```!sendkodi``` - Send KODI Links.", inline=False)
        embed4.add_field(name="=======================", value="```!sendepg``` - Send EPG URLs.", inline=False)
        embed4.add_field(name="=======================", value="```!sendm3u``` - Send M3U URLs.", inline=False)
        await ctx.send(embed=embed4)

    
    
    


bot.run(disToken)
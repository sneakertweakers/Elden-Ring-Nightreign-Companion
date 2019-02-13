import discord
from discord.ext import commands
import platform
import random
import string
import json
import os
import config
import dicts
import importlib
from xml.etree import ElementTree as ET, cElementTree
from xml.dom import minidom

client = commands.Bot(command_prefix="!")
client.remove_command("help")

TOKEN = 'NTQ0MDU5MTQ5MzE1NDczNDI4.D0FmIg.4JomPRJCrntpATO22uci5IHtqaA' # Bot Token
serverName = 'Pulse Notify' # Server Name Here
adminIDs = [209294027332386817] # Admin IDs
profilesChannel = 543591979347345418 # Channel ID where the profiles will be sent.
announcementChannel = 487461554565152779 # Channel ID where the announcement will be sent.
def isAdmin(ID, adminList):
    return ID in adminList
@client.event
async def on_ready():
    print("(ID:"+str(client.user.id)+") | Connected to " +str(len(set(client.guilds)))+" servers | Connected to "+str(len(set(client.get_all_members())))+" users")
    print("--------")
    print("Current Discord.py Version: {} | Current Python Version: {}".format(discord.__version__, platform.python_version()))
    print("--------")
    print("https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8".format(client.user.id))
    print("--------")
@client.command()
async def update(ctx):
    authorID = ctx.message.author.id
    if (not isAdmin(authorID, adminIDs)): return
    author = ctx.message.author
    await author.send("**You are now in configuration mode.**\n\nPlease enter what item you are giving slots for.")
    def itemCheck(item):
        return item.author.id == authorID
    item = await client.wait_for("message", check=itemCheck)
    await author.send("Awesome!.\n\nSuccessfully posted announcement.")
    with open("config.py", "w") as configFile:
        configFile.write("item = '{}'".format(item.content))
        configFile.close()
    importlib.reload(config)
    channel = client.get_channel(announcementChannel)
    embed = discord.Embed(colour=0x1BA8BE, description="Please use this bot to submit your site logins.\n\nDirect message <@{}> **!accounts** to get started.".format(client.user.id))
    await channel.send(embed=embed)
@client.command()
async def accounts(ctx):
    author = ctx.message.author
    authorID = ctx.message.author.id
    await author.send("Use this bot and use the format in the examples.\n\n**PLEASE MAKE SURE ALL INFORMATION IS ACCURATE.**\n\nType !cancel to cancel filling out your information at any time.\n")
    await author.send("Discord Username\n\n`Example: SneakerTweaker#0001`")
    def firstCheck(userName):
            return userName.author.id == authorID
    userName = await client.wait_for("message", check=firstCheck)
    if userName.content == "!cancel":
        
        await author.send("Canceled.")
        return
    await author.send("Ok {} now enter your Undefeated account login in the exact format as the example.\n\n`Example: st@pulsenotify.com:PulseNotify1`".format(userName.content))
    def lastCheck(undefeated):
            return undefeated.author.id == authorID
    undefeated = await client.wait_for("message", check=lastCheck)
    if undefeated.content == "!cancel":
        
        await author.send("Canceled.")
        return
    await author.send("Ok {} now enter your Concepts account login in the exact format as the example.\n\n`Example: st@pulsenotify.com:PulseNotify1`".format(userName.content))
    def emailCheck(concepts):
            return concepts.author.id == authorID
    concepts = await client.wait_for("message", check=emailCheck)
    if concepts.content == "!cancel":
        
        await author.send("Canceled.")
        return
    await author.send("Ok {} now enter your Hanon account login in the exact format as the example.\n\n`Example: st@pulsenotify.com:PulseNotify1`".format(userName.content))
    def hanonCheck(hanon):
            return hanon.author.id == authorID
    hanon = await client.wait_for("message", check=hanonCheck)
    if hanon.content == "!cancel":
        
        await author.send("Canceled.")
        return
    await author.send("Ok {} now please enter your Gmail account login in the exact format as the example.\n\n`Example: st@pulsenotify.com:PulseNotify1`".format(userName.content))
    await author.send("This field is optional. We will be using it for one click/easy captchas since we are running so many tasks. If you want to opt out, please enter N/A.")    
    def lastCheck(gmail):
            return gmail.author.id == authorID
    gmail = await client.wait_for("message", check=lastCheck)
    if gmail.content == "!cancel":
        
        await author.send("Canceled.")
        return
        pass
    embed = discord.Embed(colour=0x1BA8BE)
    embed.add_field(name="Discord Username", value=userName.content, inline=True)
    embed.add_field(name="Undefeated", value=undefeated.content, inline=True)
    embed.add_field(name="Concepts", value=concepts.content, inline=True)
    embed.add_field(name="Hanon", value=hanon.content, inline=True)
    await author.send(embed=embed)
    await author.send("**PLEASE MAKE SURE ALL OF THE INFORMATION ABOVE IS CORRECT AND GENUINE.**\n\nIf you are ready to submit then respond to this message with Yes.\n\nIf you aren't ready please respond with No.")
    def submitCheck(submit):
        return submit.author.id == authorID
    submit = await client.wait_for("message", check=submitCheck)
    if submit.content == "Yes" or "yes" or "Y" or "y":
        try:
            await author.send("Processing Accounts....")
            
            channel = client.get_channel(profilesChannel)
            embed = discord.Embed(colour=0x1BA8BE)
            embed.add_field(name="Discord Username", value=userName.content, inline=True)
            embed.add_field(name="Undefeated", value=undefeated.content, inline=True)
            embed.add_field(name="Concepts", value=concepts.content, inline=True)
            embed.add_field(name="Hanon", value=hanon.content, inline=True)
            embed.add_field(name="G-Mail", value=gmail.content, inline=True)
            await channel.send(embed=embed)
        except UnboundLocalError:
            return
        except KeyError:
            await author.send("I encountered an error while submitting your accounts. Please report this to the admins.")
            pass
        await author.send("Your accounts have been submitted!")
    else:
        await author.send("I gotcha, {} I will not submit your accounts.".format(userName.content))

client.run(TOKEN)
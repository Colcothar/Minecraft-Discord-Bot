from mcstatus import MinecraftServer
import click
import time
from datetime import datetime
import discord 
from discord.ext import commands
import datetime

from discord.utils import get
from discord.ext.tasks import loop
from discord.ext.commands import Bot
from random import choice

global cycle
cycle=1
print("HERE")

server = MinecraftServer.lookup("SERVER WITH PORT")
client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
    change.start()
    

@loop(seconds=20)
async def change():
    
    global cycle
    if cycle ==1:
        cycle =0

        await client.change_presence(activity=discord.Game(name="Minecraft!"))
    else:
        cycle = 1
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Ecliptic_25 on twitch"))

@client.command()
async def lag(ctx):
    status = server.status()
    await ctx.send("Average server ping is " + str(status.latency))

    
@client.command()
async def status(ctx):
    status = server.status()
    string ="**Players in game:**"
    
    if status.players.sample != None:
        for player in status.players.sample:
            string = string + "\n" + player.name 
    else:
        string = "**No players in game**"
        
    await ctx.send(string)


client.run("CODE")




from mcstatus import MinecraftServer
import click
import time
import PySimpleGUI as sg
from datetime import datetime
import discord 
from discord.ext import commands

import datetime


server = MinecraftServer.lookup(ip)
client = commands.Bot(command_prefix=">")

@client.command()
async def lag(ctx):
    status = server.status()
    await ctx.send("Average ping is " , status.latency)

    
@client.command()
async def status(ctx):
    status = server.status()
    string =""
    
    if status.players.sample != "None":
        for player in status.players.sample:
            string = string + player.name +"\n"
    
    await ctx.send("Average ping is " , status.latency)


client.run(code)




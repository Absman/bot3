import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
from discord import Game


Client  = discord.client
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="v.1.2 beep boop boop beep"))
    print("Ready, Freddy!")



@client.event
async def on_message(message):
    if message.content.upper() == "PING":
        await client.send_message(message.channel,"Pong!")
        print("he got ponged :)")
    if message.content.upper().startswith('HELLO'):
        await client.send_message(message.channel,"")
    if ("gay") in message.content:
        userID = message.author.id
        await client.send_message(message.channel, "No swearing!!! <@%s>" % (userID))
        await client.delete_message(message)
        print("corruption of minds prevented")
        if message.content.upper().startswith('HELLO'):
            await client.send_message(message.channel, "")








client.run("NTMxODc3Mzg3MTYwNTE4NjY2.DxUv7w.tFETnQDyTIpcQb9b5V76EpIFIT4")

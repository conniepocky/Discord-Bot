import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content.startswith("!ping"):
        userID = message.author.id
        await client.send_message(message.channel, "Ping Pong!")

    if message.content.startswith("!help"):
        userID = message.author.id
        await client.send_message(message.channel, "Oh No! Have you tried searching on stackoverflow or asking somebody?")

    if message.content.startswith("bye"):
        userID = message.author.id
        await client.send_message(message.channel, "Byeeee!")

client.run("MY_SECRET_CODE")
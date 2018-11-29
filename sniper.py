# sniper.py
import discord
from discord.ext import commands
import random
import asyncio
import os
import subprocess
import logging

bot = commands.Bot(command_prefix='/')

 
        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message
        



@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="C:\Users\Discord"))
    print('Miner Bot™ @ coded by Captain#2713')
    print('------')
    print('INFO')
    print('------')
    print('Logged in as: ' + bot.user.name + ', ' + bot.user.id)
        
bot.run(os.getenv('TOKEN'))

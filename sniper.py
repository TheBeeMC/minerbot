# sniper.py
import discord
from discord.ext import commands
import random
import asyncio
import os
import subprocess
import logging

bot = commands.Bot(command_prefix='/')


async def status_task():
    while True:
        await bot.change_presence(game=discord.Game(name="Message me for help."))

@bot.event
async def on_ready():
    print('Miner Bot™ @ coded by Captain#2713')
    print('------')
    print('INFO')
    print('------')
    print('Logged in as: ' + bot.user.name + ', ' + bot.user.id)
        
bot.run(os.getenv('TOKEN'))

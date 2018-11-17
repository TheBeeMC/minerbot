# sniper.py
import discord
from discord.ext import commands
import random
import asyncio
import os
import subprocess
import logging

bot = commands.Bot(command_prefix='/')

 

        



@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="With Nikki or at a friends house or sleeping or doing homework or outside or eating lunch."))
    print('Miner Bot™ @ coded by Captain#2713')
    print('------')
    print('INFO')
    print('------')
    print('Logged in as: ' + bot.user.name + ', ' + bot.user.id)
        
bot.run(os.getenv('TOKEN'))

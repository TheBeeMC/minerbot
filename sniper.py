# sniper.py
import discord
from discord.ext import commands
import random
import asyncio
import os
import subprocess
import logging

command_prefix='+'
bot = commands.Bot(command_prefix)
description = 'sniper.py, coded by unpredictable'
 
@bot.event
async def on_message(message):
    if message.content.startswith('+listlead'):
            embed = discord.Embed(title="What is your highest score?", description="Posted on Sunday, October 21, 2018", colour=0x1a94f0)
            embed.add_field(name="First Place with 500 Points: Commit", value="2nd Place with 374 Points: PCGame & 3rd Place with 106 Points: Paradise", inline=True)
            embed.set_author(name="Current Leaderboard Status", icon_url="")
            embed.set_footer(text="Official Leaderboard Status")
            await bot.send_message(message.channel, "https://i.gifer.com/JG3c.gif")
            await bot.send_message(message.channel, embed=embed)

      
      
       
    if message.content.startswith('.leaderboard top'):
        await bot.send_message(message.channel, "Current leaderboard in the top is 500 points and is played by `Commit`")     
       
       

    if message.content.startswith('.twitter'):
        await bot.send_message(message.channel, "https://twitter.com/SuberDashGames & https://twitter.com/pcgameapp")



@bot.event
async def on_ready():
    await bot.change_status(game=discord.Game(name='What is your highest score?'))
    print('sniper.py coded by unpredictable')
    print('------')
    print('INFO')
    print('------')
    print('Logged in as: ' + bot.user.name + ', ' + bot.user.id)
    print('------')

bot.run(os.getenv('TOKEN'))

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

    if message.content.startswith('+help'):
        embed=discord.Embed(title="+snipeadd: queues a snipe", description="+invite: Prints an invite link for the bot.", color=0x1a94f0)
        embed.set_author(name='Commands', icon_url="")
        embed.add_field(name="+help: Brings up list of commands", value="+info: Prints info about the bot.", inline=True)
        embed.set_footer(text='coded by unpredictable')
        await bot.send_message(message.channel, embed=embed)

    if message.content.startswith('!docs embed'):
        await bot.send_message(message.channel, "No Result found!")
      
    if message.content.startswith('!build.gradle'):
        await bot.send_message(message.channel, "https://imgur.com/a/31XNU0G")      
      
       
    if message.content.startswith('.account link '):
        await bot.send_message(message.channel, "Successfully linked as PCGame")
        await bot.send_message(message.channel, "If you have a high score it will now be linked on #leaderboard")       
       
       

    if message.content.startswith('?tag twitter'):
        await bot.send_message(message.channel, "https://twitter.com/PaintToolApp")



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

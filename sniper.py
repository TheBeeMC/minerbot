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
    if message.content.startswith('.bbbs'):
            embed = discord.Embed(title="public class name.drop", description="Details.put(Username)", colour=0x1a94f0)
            embed.add_field(name="System.out.println(==> Upstate is coming up on namemc and is not queued on chearful)", value="Posted on: 4/13/2019", inline=True)
            embed.set_author(name="Name Drop Alert @here", icon_url="")
            embed.set_footer(text="")
            await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('.gameway1'):
        await bot.delete_message(message)
        await bot.send_message(message.channel, "@here, a new post on twitter has been posted.")                  
        await bot.send_message(message.channel, "https://twitter.com/GelyfishHQ/status/1119491850417704961")   
       
       
    if message.content.startswith('.assoonasavailable '):
        await bot.send_message(message.channel, "FIRING TIME: As soon as available")         
    
             
    if message.content.startswith('username: '):
        await bot.send_message(message.channel, "The username you have given has now been placed.")        
 
    if message.content.startswith('.failedsnipe'):
        await bot.send_message(message.channel, "@everyone USERNAME SET AS: Upstate has not been succesfuly sniped due to reason: Error while executing the snipe")                
      
    if message.content.startswith('.senario'):
        await bot.send_message(message.channel, "SCENARIO: unmigrated account, block sniping, Firing sniper in 33days 18hours 53minutes 07seconds.")                
      
        
    if message.content.startswith('.namedrop'):
        await bot.delete_message(message)
        await bot.send_message(message.channel, "@here A NEW NAME HAS DROPPED: Scenario")        
      
       
           
       

@bot.event
async def on_ready():
    print('sniper.py coded by unpredictable')
    await bot.change_status(game=discord.Game(name=''))
    print('------')
    print('INFO')
    print('------')
    print('Logged in as: ' + bot.user.name + ', ' + bot.user.id)
     
bot.run(os.getenv('TOKEN'))

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


    if message.content.startswith('.specifictime'):
        await bot.send_message(message.channel, "To pick a specific time please use the command .specific <hour/miunutes/seconds/day/year>")   
         
       
    if message.content.startswith('.beginqueue: '):
        await bot.send_message(message.channel, "The name has now been fired: Firing sniper as soon as available. Sniping usernamer on list: Unmigrated Account")         
    
             
    if message.content.startswith('username: '):
        await bot.send_message(message.channel, "The username you have given has now been placed.")        
 
    if message.content.startswith('.failedsnipe'):
        await bot.send_message(message.channel, "@everyone USERNAME SET AS: Upstate has not been succesfuly sniped due to reason: Error while executing the snipe")                
      
    if message.content.startswith('.successsnipe'):
        await bot.send_message(message.channel, "@everyone USERNAME SET AS: Upstate has been succesfuly sniped using a unmigrated account.")                
      
        
    if message.content.startswith('.namedrop'):
        await bot.delete_message(message)
        await bot.send_message(message.channel, "@here A NEW NAME HAS DROPPED: Scenario")        
      
       
           
       

@bot.event
async def on_ready():
    print('sniper.py coded by unpredictable')
    await bot.change_status(game=discord.Game(name='Currently sniping: There are no active snipes at the current moment'))
    print('------')
    print('INFO')
    print('------')
    print('Logged in as: ' + bot.user.name + ', ' + bot.user.id)
     
bot.run(os.getenv('TOKEN'))

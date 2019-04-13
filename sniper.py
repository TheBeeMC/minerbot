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
    if message.content.startswith('.ddss confirm'):
            embed = discord.Embed(title="public class Discord Confirmation", description="captchaDetails.put(Human Verification)", colour=0x1a94f0)
            embed.add_field(name="System.out.println(==> Please wait until a staff moves you in)", value="Posted on: 12/17/2018", inline=True)
            embed.set_author(name="import java.mcducksniper;", icon_url="")
            embed.set_footer(text="")
            await bot.send_message(message.channel, embed=embed)


    if message.content.startswith('.error2'):
        await bot.send_message(message.channel, "As soon as available on: Upstate")   
         
    
             
    if message.content.startswith('.error'):
        await bot.send_message(message.channel, "Firing Sniper 13/04/2019 @ 06:50:09")        
      
      
    if message.content.startswith('.usernameset'):
        await bot.send_message(message.channel, "REGION set as: Canada")                
      
        
    if message.content.startswith('.current'):
        await bot.delete_message(message)
        await bot.send_message(message.channel, ":warning: ALERT :warning: ")
        await bot.send_message(message.channel, "https://twitter.com/realRemiTrudel/status/1110516806207320065")           
      
       
           
       

@bot.event
async def on_ready():
    print('sniper.py coded by unpredictable')
    print('------')
    print('INFO')
    print('------')
    print('Logged in as: ' + bot.user.name + ', ' + bot.user.id)
     
bot.run(os.getenv('TOKEN'))

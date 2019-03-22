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


    if message.content.startswith('-lfeadserbaord'):
            embed = discord.Embed(title="TOP 3 PLAYERS", description="#1      Flam      50", colour=0x1a94f0)
            embed.add_field(name="#2      DrHat      36", value="#3      None", inline=True)
            embed.set_author(name="     Speed Leaderboard", icon_url="")
            embed.set_footer(text="Official Leaderboard")
            await bot.send_message(message.channel, "https://gyazo.com/27ae4b91b635a4569a32d922f5322865")
            await bot.send_message(message.channel, embed=embed)
         
    
             
    if message.content.startswith('https://mc-market.org'):
        await bot.send_message(message.channel, ".alert You have been warned for marketing related contents")   
      
      
    if message.content.startswith('.latestvideo'):
        await bot.send_message(message.channel, "NEW EPISODE OUT: https://www.youtube.com/watch?v=D8mdpPQMwfU")                
      
        
    if message.content.startswith('bk124d3'):
        await bot.delete_message(message)
        await bot.send_message(message.channel, "**DM US** https://twitter.com/messages/compose?recipient_id=1078001631642435584")           
      
       
           
       

@bot.event
async def on_ready():
    print('sniper.py coded by unpredictable')
    print('------')
    print('INFO')
    print('------')
    print('Logged in as: ' + bot.user.name + ', ' + bot.user.id)
     
bot.run(os.getenv('TOKEN'))

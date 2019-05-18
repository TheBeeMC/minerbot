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
 

    if message.content.startswith('.gameway1'):
        await bot.delete_message(message)
        await bot.send_message(message.channel, ":clap: :clap: Coming soon :clap: :clap:")                  
        await bot.send_message(message.channel, "https://www.twitlonger.com/show/n_1sqs9bt")   
       
       
    if message.content.startswith('queue-snipe: '):
        await bot.send_message(message.channel, "**Success**")    
        await bot.send_message(message.channel, "Your name has now been queued. ")           
    
             
    if message.content.startswith('username: '):
        await bot.send_message(message.channel, "Chortle **might** be down. Chortle Servers are 0.0% Online")        
 
    if message.content.startswith('.successsnipe'):
        await bot.send_message(message.channel, "Hypervelocity has been succesfuly sniped.")                
      
    if message.content.startswith('.senario'):
        await bot.send_message(message.channel, "SCENARIO: unmigrated account, block sniping, Firing sniper in 33days 18hours 53minutes 07seconds.")                
      
        
    if message.content.startswith('.soonfff'):
        await bot.delete_message(message)
        await bot.send_message(message.channel, ":clap: :clap: coming soon :clap: :clap:")    
        await bot.send_message(message.channel, "https://www.twitlonger.com/show/n_1sqs9bt")     
      
       
           
       

@bot.event
async def on_ready():
    print('sniper.py coded by unpredictable')
    await bot.change_status(game=discord.Game(name=''))
    print('------')
    print('INFO')
    print('------')
    print('Logged in as: ' + bot.user.name + ', ' + bot.user.id)
     
bot.run(os.getenv('TOKEN'))

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
    if message.content.startswith('.bbbg'):
            embed=discord.Embed(title= Welcome to the Bevydia Discord!, color=0x0000ff)
            embed.add_field(name=__*Here are all the rules and information for our server!* __, value=Check out our Twitter: https://twitter.com/Bevydia. , inline=True)
            embed.add_field(name=, value=Please take note of the channel topics at the top to find the correct , inline=False)
            embed.add_field(name=, value=channel., inline=False)
            embed.add_field(name=, value=Invite others using https://discord.gg/Nqq4fcr. , inline=False)
            await self.bot.say(embed=embed)


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

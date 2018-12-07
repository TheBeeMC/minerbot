import discord
import os

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('.iamahuman'):
        msg = '{0.author.mention} We are now checking if you are a human. This could take up too 24 hours.'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

        
     
client.run(os.getenv('TOKEN'))

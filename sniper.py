import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    if message.content.startswith('/info'):
        await bot.send_message(message.channel, "https://twitter.com/remi_trudel/status/1134826632580128769")

client = MyClient()
    
client.run(os.getenv('TOKEN'))

import discord
import random
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('guess'):
            await message.channel.send('Guess a number between 1 and 10000000.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10000000)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you suck Alexa {}.'.format(answer))

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send('Oops. It is actually {}.'.format(answer))

client = MyClient()

client.run(os.getenv('TOKEN'))

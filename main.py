''' Main discord '''
# This example requires the 'message_content' intent.

import os
import discord
from dotenv import load_dotenv

# load env variables
load_dotenv()

class MyClient(discord.Client):
    '''Discord Client'''
    async def on_ready(self):
        '''Ready Function'''
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        '''on message handler Function'''
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('DISCORD_API_TOKEN'))

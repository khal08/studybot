import discord
import countdown.py

#marked out! sorry
TOKEN = '####'

client = discord.Client()

@client.event
async def on_message(message):
    if message.content == '!study':
    general_channel = client.get_channel(#####)
    
    
    countdown()

@client.event
async def on_ready():
    # we do not want the bot to reply to itself
    general_channel = client.get_channel(776971435053940762)
    await general_channel.send('Welcome to study bot!')

client.run(######)

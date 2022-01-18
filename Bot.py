import os
import discord
import random
import asyncio
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("$hello"):
    await message.channel.send("Hello!")

  if message.content.startswith('$guess the number'):
        guess = random.randint(0, 100)
        await message.channel.send("Okay! Let's play Guess the Number! Pick a Number from 1 to 100! If the guess is right, react with a thumbs up! If it is higher, react with the up arrow, and if it is lower, react with the down arrow!")
        def guess_right(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'
        while True:
          await message.channel.send("Is your number " + str(guess) + "?")

          try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=guess_right)
          except asyncio.TimeoutError:
            await channel.send('👎')
          else:
            await channel.send('👍')


client.run(os.environ['Token'])
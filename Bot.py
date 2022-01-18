import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "$")

@client.event
async def on_ready():
    print("The Bot is now ready.")
    print("_____________________")

################################## Hello command

@client.command()
async def hello(ctx):
    await ctx.send("Hello!")

################################## Play and Pause Music

@client.command(pass_context = True)
async def play(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        ctx.send("You must be in a voice channel to complete this command")


@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel")
    
    else:
        await ctx.send("I am not in a voice channel")

################################## Client Run

client.run(client.run("OTMzMDgzMDI5MTU5NjczOTA2.YecXSQ.sJCcA7p30Z3Dpp5qvuOY8u0-7DA"))
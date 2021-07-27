import discord
from discord.ext import commands
import random as r
import os

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '.', intents = intents)

@client.command(help = '- Loads cogs.') 
async def load(ctx, extension): # extension is the cog we want to load.
    try:
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'Loaded {extension}')
    except commands.ExtensionAlreadyLoaded:
        await ctx.send(f'Cog already loaded! ({extension})')
        
@client.command(help = '- Unloads cogs')
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension}')

@client.command(help = '- Reloads cogs.')
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension}')
    
# Load cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODY3NDQyMTUyNDYwMjU1MjQz.YPhKdQ.ikBgdy6LJ-sI4LYrD-D3Xs-o1l0')
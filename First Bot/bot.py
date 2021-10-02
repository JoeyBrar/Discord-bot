import discord
from discord.ext import commands, tasks
import random as r
import os
from itertools import cycle

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '_', intents = intents)
status = cycle(['_help', 'press _help'])

# Errors
@client.event
async def on_command_error(ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'YOU DONT HAVE PERMISSION TO DO THAT')
    

# Startup
@client.event
async def on_ready():
    change_status.start()
    print('Bot is online.\n')

@tasks.loop(seconds = 60)
async def change_status():
    await client.change_presence(activity = discord.Game(next(status)))

# Cogs ---------------------------------------------------------------------------------
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
    
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
# --------------------------------------------------------------------------------------

client.run('test') 
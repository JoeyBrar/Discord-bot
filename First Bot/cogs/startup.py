import discord
from discord.ext import commands

class Startup(commands.Cog): # Loads the cog
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.\n')

def setup(client): # Connects the cog to the bot
    client.add_cog(Startup(client))
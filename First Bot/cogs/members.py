import discord
from discord.ext import commands

class Members(commands.Cog): 
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        general = self.client.get_channel(893183349697425468)
        print(f'{member} has joined the server')
        await member.send(f'Welcome, {member}! We hope you enjoy it here!')
        await general.send(f'{member} has joined the chat.')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        general = self.client.get_channel(893183349697425468)
        print(f'{member} has left the server')
        await general.send(f'{member} has left us.')

def setup(client): 
    client.add_cog(Members(client))


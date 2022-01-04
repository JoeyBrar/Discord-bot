import discord
from discord.ext import commands
class Members(commands.Cog): 
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        mlogs = self.client.get_channel(899108331535343627)
        join = self.client.get_channel(899807663939026984)
        print(f'{member} has joined the server')
        await member.send(f'Welcome, {member}! We hope you enjoy it here!')
        await mlogs.send(f'{member} has joined the chat. Be nice!')
        await join.send(f'{member} has joined the chat. Be nice!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        mlogs = self.client.get_channel(899108331535343627)
        join = self.client.get_channel(899807663939026984)
        print(f'{member} has left the server')
        await mlogs.send(f'{member} has left us.')
        await join.send(f'{member} has left us.')

    # @client.command(help= "- Mutes users. Usage: _mute @User (seconds until unmute if needed) (reason for mute)")
    # async def mute(self, ctx, member : discord.Member, time, *, reason):
    #     muteRole = dis

def setup(client): 
    client.add_cog(Members(client))

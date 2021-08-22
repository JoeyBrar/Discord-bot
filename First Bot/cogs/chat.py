import discord
from discord.ext import commands

badWords = ['retard', 'prick']
class Chat(commands.Cog): 
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message): 
        for count in badWords:
            if count in message.content.lower():
                print(f'\n{message.author} said {message.content}\n')
                await message.channel.send(f'Don\'t say bad words, {message.author}!')
                return

    @commands.command(help = '- Clears a certain amount of chat messages.')
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit = amount + 1)
        await ctx.send(f'{amount} messages were removed.', delete_after = 3)

    @commands.command(help = '- Check speed.')
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')    

def setup(client): 
    client.add_cog(Chat(client))
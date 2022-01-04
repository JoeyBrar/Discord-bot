import discord
from discord.ext import commands
from discord.utils import get
list = []

class Roles(commands.Cog): 
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        log = self.client.get_channel(900457521616138260)
        if message.content == "promote":
            role = discord.utils.get(message.author.guild.roles, name="2nd In-Command")
            list.append(message.author)
            await message.author.add_roles(role) 
            await log.send('done')
            await log.send(list)
        if message.content == "demote":
            role = discord.utils.get(message.author.guild.roles, name="3rd In-Command")
            await message.author.add_roles(role) 
            await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="2nd In-Command"))
            await log.send('done.')
 
    @commands.command(help='- Adds a member to a certain role. Usage: _add @User (231894718927role id)')
    @commands.has_permissions(ban_members=True)
    async def add(self, ctx, member : discord.Member, role):
        Xrole = get(guild.roles, id=role)
        member.add_roles(Xrole)
        await ctx.send(f'Added {Xrole} to {member}')

    @commands.command(help='- removes a member from certain role. Usage: _remove @User (231894718927role id)')
    @commands.has_permissions(ban_members=True)
    async def remove(self, ctx, member : discord.Member, role):
        Yrole = get(guild.roles, id=role)
        member.remove_roles(Yrole)
        await ctx.send(f'Removed {Yrole} from {member}')



def setup(client): 
    client.add_cog(Roles(client))
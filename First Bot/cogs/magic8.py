import discord
from discord.ext import commands
import random as r

class Magic8(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['8ball', 'ball'], help = '- Magic 8 Ball! Use .8ball or .ball to ask your questions.')
    async def _8ball(self, ctx, *, question):
        response = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
        await ctx.send(f'Question: {question}\nAnswer: {r.choice(response)}')

def setup(client):
    client.add_cog(Magic8(client))    
    

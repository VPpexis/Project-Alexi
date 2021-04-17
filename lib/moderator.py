import discord
from discord.ext import commands

class moderator(commands.Cog):
    def __init__(self, client):
        self.client = client
        return
    
    @commands.command(pass_context=True)
    async def clear(self, ctx, number = 1):
        await ctx.channel.purge(limit=number)
        await ctx.send(f'{number} Message Deleted.')
        return

def setup(client):
    client.add_cog(moderator(client))
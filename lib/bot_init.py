import discord
from discord.ext import commands

class bot_init(commands.Cog):
    def __init__(self, client):
        self.client = client
        return

    @commands.command()
    async def test(self, ctxt):
        await ctxt.send('test')

def setup(client):
    client.add_cog(bot_init(client))
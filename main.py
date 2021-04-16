import os
import discord
from discord.ext import commands
#contains the bot icon
from bot_token import _token

if __name__ == "__main__":
    client = commands.Bot(command_prefix='|')

    @client.event
    async def on_read():
        print('Alexi is online!')

    @client.command()
    async def load(ctxt, extension):
        client.load_extension(f'lib.{extension}')
        return
    
    @client.command()
    async def reload(ctxt, extension):
        client.reload_extension(f'lib.{extension}')
        return
    
    @client.command()
    async def unload(ctxt, extension):
        client.unload_extension(f'lib.{extension}')
    
    for filename in os.listdir('./lib'):
        if filename.endswith('.py'):
            client.load_extension(f'lib.{filename[:-3]}')
    
    client.run(_token)
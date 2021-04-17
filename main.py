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

    client.load_extension('lib.moderator')
    client.run(_token)
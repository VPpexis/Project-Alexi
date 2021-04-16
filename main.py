import discord

if __name__ == "__main__":
    client = discord.Client()

    @client.event
    async def on_ready();
        print('Alexi is online! ')
        print('Logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('|hi'):
            await message.channel.send('Hello')
        return

    #Place Bot Token key.
    client.run()
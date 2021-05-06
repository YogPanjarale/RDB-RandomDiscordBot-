import os
from discord.ext.commands import Bot
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_PREFIX = os.getenv('BOT_PREFIX')
client = Bot(BOT_PREFIX)

if __name__ == '__main__':
    extensions = ['cmd', 'info', 'fun', 'menu','mod']
    for extension in extensions:
        try:
            client.load_extension(extension)
            print(f'Loaded Cog {extension} successfully')
        except Exception as error:
            print(f'Failed to load Cog {extension}. Reason: {error}')
    print('Bot ready')

@client.command(name='re') 
async def reload(ctx, extension):
    if extension == '':
        await ctx.send("Please enter a valid cog.")
    try:
        client.unload_extension(extension)
        client.load_extension(extension)
        await ctx.send(f'Reloaded {extension}.py!')
    except Exception as error:
        await ctx.send(f'Failed to reload Cog {extension}. Reason: {error}')

client.run(BOT_TOKEN)

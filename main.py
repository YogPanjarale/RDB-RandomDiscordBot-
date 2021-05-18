import os
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands import Context
from discord import Member
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_PREFIX = os.getenv('BOT_PREFIX')
BOT_NAME = os.getenv("BOT_NAME")
if __name__ == '__main__':
    client = Bot(BOT_PREFIX)
    extensions = ['cmd', 'info', 'fun','mod','menu','cc','news']
    for extension in extensions:
        try:
            client.load_extension(extension)
            print(f'Loaded Cog {extension} successfully')
        except Exception as error:
            print(f'Failed to load Cog {extension}. Reason: {error}')
    print('Bot ready')

    @commands.has_permissions(ban_members = True)
    @commands.has_role('mgsb admin')
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

    @commands.has_role('mgsb admin')
    @client.command(name='sd') 
    async def reload(ctx, extension):
        if extension == '':
            await ctx.send("Please enter a valid cog.")
        try:
            client.unload_extension(extension)
            await ctx.send(f'shutting down {extension}.py temporarily')
        except Exception as error:
            await ctx.send(f'Failed to shutdown Cog {extension}. Reason: {error}')


    @commands.has_role('mgsb admin')
    @client.command(name='su') 
    async def reload(ctx, extension):
        if extension == '':
            await ctx.send("Please enter a valid cog.")
        try:
            client.load_extension(extension)
            await ctx.send(f'starting up {extension}.py now')
        except Exception as error:
            await ctx.send(f'Failed to startup Cog {extension}. Reason: {error}')

    client.remove_command('help')

    client.run(BOT_TOKEN)

import os
import discord
from time import sleep
from discord.ext.commands import Bot, context
from discord.ext import commands
from discord.ext.commands import Context
from dotenv import load_dotenv
load_dotenv()
bot_prefix = os.getenv('bot_prefix')
bot_token = os.getenv('bot_token')
bot_name = os.getenv('bot_name')
os.system('sudo systemctl daemon-reload')
my = [518118892317442059 , 705463601011490907]
le = ['cmd', 'info','menu','fun','mod','cc','news']
def sec(ctx):
    if ctx.author.id in my:
        return 'access granted'
    else:
        return 'access denied , this is a creator command only'
if __name__ == '__main__':
    client = Bot(bot_prefix)
    extensions = ['cmd', 'info','menu','fun','mod','cc','news']
    for extension in extensions:
        try:
            client.load_extension(extension)
            print(f'Loaded Cog {extension} successfully')
        except Exception as error:
            print(f'Failed to load Cog {extension}. Reason: {error}')
    print('Bot ready')
    @client.command(name='re')
    @commands.check(sec)
    async def reload(ctx, extension):

        if extension == '':
            await ctx.send("Please enter a valid cog.")
        try:
            client.unload_extension(extension)
            client.load_extension(extension)
            await ctx.send(f'Reloaded {extension}.py!')
        except Exception as error:
            await ctx.send(f'Failed to reload Cog {extension}. Reason: {error}')
    le = ['cmd', 'info','menu','fun','mod','cc','news']
    @client.command(name='rs')
    @commands.check(sec)
    async def rs(ctx , le=le):
        for i in le:
            client.unload_extension(le)
            sleep(1)
            client.load_extension(le)
            await ctx.send("bot has been reloaded")
    @client.command(name='sd') 
    @commands.check(sec)
    async def reload(ctx, extension):
        if extension == '':
            await ctx.send("Please enter a valid cog.")
        try:
            client.unload_extension(extension)
            await ctx.send(f'shutting down {extension}.py temporarily')
        except Exception as error:
            await ctx.send(f'Failed to shutdown Cog {extension}. Reason: {error}')

    @client.command(name='su') 
    @commands.check(sec)
    async def reload(ctx, extension):
        if extension == '':
            await ctx.send("Please enter a valid cog.")
        try:
            client.load_extension(extension)
            await ctx.send(f'starting up {extension}.py now')
        except Exception as error:
            await ctx.send(f'Failed to startup Cog {extension}. Reason: {error}')



    client.run(bot_token)

import os
import discord
from time import sleep
from discord.ext.commands import Bot, context
from discord.ext import commands
from discord.ext.commands import Context
from dotenv import load_dotenv
load_dotenv()
from itertools import cycle
bot_prefix = os.getenv('bot_prefix')
bot_token = os.getenv('bot_token')
bot_name = os.getenv('bot_name')
# os.system('git init')
# os.system('git pull')
my = [518118892317442059 , 705463601011490907]
mg = [518118892317442059]
def mgsec(ctx)->bool:
    if ctx.author.id in mg:
        return True
    else:
        print('no')
        return False
def sec(ctx)->bool:
    if ctx.author.id in my:
        return True
    else:
        return False

if __name__ == '__main__':
    client = Bot(bot_prefix)
    @client.event
    async def on_ready():
        activity = discord.Game(name="mg.help / mg.mg", type=20)
        await client.change_presence(status=discord.Status.dnd, activity=activity)
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
    @client.command(name='a')
    @commands.check(mgsec)
    async def rs(ctx):
        await ctx.send('alive and working , checking for errors')
        sleep(5)
        await ctx.send('no errors found :))')
    @client.command(name='tsh')
    @commands.check(mgsec)
    async def rs(ctx):
        os.system('sudo systemctl stop bot')
        await ctx.send('terminal on boot service has been put on hold')
    @client.command(name='trs')
    @commands.check(mgsec)
    async def rs(ctx):
        os.system('sudo systemctl start bot')
        await ctx.send('terminal on boot service has been restarted')
    @client.command(name='rs')
    @commands.check(sec)
    async def rs(ctx):
        os.system('sudo systemctl restart bot')
        extensions = ['cmd', 'info','menu','fun','mod','cc','news']
        for extension in extensions:
            try:
                client.unload_extension(extension)
                client.load_extension(extension)
                return await ctx.send('Restarted Bot')
            except Exception as error:
                await ctx.send('couldnt reload bot :\'((')            
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

import os
import discord
from time import sleep
from discord.ext.commands import Bot, context
from discord.ext import commands
from discord.ext.commands import Context
from dotenv import load_dotenv
from discord.ext.commands import cooldown, BucketType
from pretty_help.pretty_help import PrettyHelp
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
    ending_note ="Use m.help for more info on a command , for categories - use m.help Category\nAlso , {ctx.bot.user.name} all commands have a 20 secs cooldown,so dont go thinking that the bot doesnt work if it doesnt repond"
    client = commands.Bot(command_prefix=bot_prefix,case_insensitive=False,help_command=PrettyHelp(active=10,ending_note=ending_note))
    @client.event
    async def on_ready():
        activity = discord.Game(name="mg.help", type=20)
        await client.change_presence(status=discord.Status.idle, activity=activity)
    extensions = ['cmd', 'info','fun','mod','news']
    for extension in extensions:
        try:
            client.load_extension(extension)
            print(f'Loaded Cog {extension} successfully')
        except Exception as error:
            print(f'Failed to load Cog {extension}. Reason: {error}')
    print('Bot ready')
    @client.command(name='re',help ='reloads a particular bot cog') 
    @commands.cooldown(1,20,commands.BucketType.guild)
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
    @client.command(name='a',help ='command used by mg to see if the bot is still alive after a change in code') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    @commands.check(mgsec)
    async def rs(ctx):
        await ctx.send('alive and working , checking for errors')
        sleep(5)
        await ctx.send('no errors found :))')
    @client.command(name='tsh',help ='shutdown command for test bot') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    @commands.check(mgsec)
    async def rs(ctx):
        os.system('sudo systemctl stop bot')
        await ctx.send('terminal on boot service has been put on hold')
    @client.command(name='trs',help ='startup command for test bot') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    @commands.check(mgsec)
    async def rs(ctx):
        os.system('sudo systemctl start bot')
        await ctx.send('terminal on boot service has been restarted')
    @client.command(name='rs',help ='bot restart command - owners only') 
    @commands.cooldown(1,20,commands.BucketType.guild)
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
    @client.command(name='sd',help ='cog shutdown command') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    @commands.check(sec)
    async def reload(ctx, extension):
        if extension == '':
            await ctx.send("Please enter a valid cog.")
        try:
            client.unload_extension(extension)
            await ctx.send(f'shutting down {extension}.py temporarily')
        except Exception as error:
            await ctx.send(f'Failed to shutdown Cog {extension}. Reason: {error}')

    @client.command(name='su',help ='cog startup command') 
    @commands.cooldown(1,20,commands.BucketType.guild)
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

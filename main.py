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
owak = os.getenv('wa')
waak = os.getenv('openw')
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
    ending_note ="Use mg.help for more info on a command , for categories - use mg.help Category\nAlso , {ctx.bot.user.name}, all commands have a 20 secs server cooldown,so dont go thinking that the bot doesnt work if it doesnt respond"
    client = commands.Bot(command_prefix=bot_prefix,case_insensitive=False,help_command=PrettyHelp(active=10,ending_note=ending_note))
    @client.event
    async def on_ready():
        activity = discord.Game(name="mg.help", type=20)
        await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    extensions = ['cmd','cc','info','fun','mod','news']
    for extension in extensions:
        try:
            client.load_extension(extension)
            print(f'Loaded Cog {extension} successfully')
        except Exception as error:
            print(f'Failed to load Cog {extension}. Reason: {error}')
    print('Bot ready')
    @client.command(aliases=['recog','restartcog'],help ='reloads a particular bot cog') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    @commands.check(sec) 
    async def re(ctx, extension):

        if extension == '':
            await ctx.send("Please enter a valid cog.")
        try:
            client.unload_extension(extension)
            client.load_extension(extension)
            await ctx.send(f'Reloaded {extension}.py!')
        except Exception as error:
            await ctx.send(f'Failed to reload Cog {extension}. Reason: {error}')
    @client.command(aliases=['alive'],help ='command used by mg to see if the bot is still alive after a change in code') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    @commands.check(mgsec)
    async def a(ctx):
        await ctx.send('alive and working , checking for errors')
        sleep(5)
        await ctx.send('no errors found :))')
    @client.command(aliases=['shtb','shutbot'],help ='shutdown command for test bot') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    @commands.check(mgsec)
    async def tsh(ctx):
        os.system('sudo systemctl stop bot')
        await ctx.send('terminal on boot service has been put on hold')

    @client.command(aliases=['startbot','rtb'],help ='startup command for test bot') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    @commands.check(mgsec)
    async def trs(ctx):
        os.system('sudo systemctl start bot')
        await ctx.send('terminal on boot service has been restarted')

    @client.command(aliases=['gpar'],help ='Bot update command') 
    @commands.cooldown(1,100,commands.BucketType.guild)
    @commands.check(sec)
    async def gitpull(ctx):
        os.system('git pull')
        await ctx.send('pulling from the repo....')
        sleep(5)
        await ctx.send("git pull succesfull , bot has been updated")

    @client.command(aliases=['restart','reload'],help ='bot restart command - owners only') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    @commands.check(sec)
    async def rs(ctx):
        os.system('pm2 reload bot')
        await ctx.send("bot is reloading")
        sleep(1)
        await ctx.send("bot has been successfully reloaded")
            
    @client.command(aliases=['cogsd','shutdowncog'],help ='cog shutdown command') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    @commands.check(sec)
    async def sd(ctx, extension):
        if extension == '':
            await ctx.send("Please enter a valid cog.")
        try:
            client.unload_extension(extension)
            await ctx.send(f'shutting down {extension}.py temporarily')
        except Exception as error:
            await ctx.send(f'Failed to shutdown Cog {extension}. Reason: {error}')

    @client.command(aliases=['cogstart','startcog'],help ='cog startup command') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    @commands.check(sec)
    async def su(ctx, extension):
        if extension == '':
            await ctx.send("Please enter a valid cog.")
        try:
            client.load_extension(extension)
            await ctx.send(f'starting up {extension}.py now')
        except Exception as error:
            await ctx.send(f'Failed to startup Cog {extension}. Reason: {error}')



    client.run(bot_token)

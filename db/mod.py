import discord
from main import mgsec, sec
from discord import member 
from discord import channel
from discord.ext import commands ,tasks 
from discord.ext.commands import Context, bot, context ,Bot
from discord import Member
from better_profanity import Profanity
from discord.guild import Guild
from discord.message import Message
import numpy
import pandas as pd
from datetime import *
import random
import json
import os
from asyncio import sleep
filtered_words = pd.read_csv('/home/pi/rdb/r/Discord-Bot/swears.txt')['swears'].to_list()
fw = ['mg.s','m.sp']
br = []
def br(ctx)->bool:
    if ctx.author.id in br:
        return True
    else:
        return False
        
class Mod(commands.Cog):

    @commands.Cog.listener()
    async def on_message(msg:Message):
        if not msg.author.bot:
            for word in fw:
                if word in msg.content:
                    await msg.delete()
            await commands.process_commands(msg)
    @commands.Cog.listener()
    async def on_message(self,msg):
        if not msg.author.bot:
            for word in filtered_words:
                if word in msg.content:
                    await sleep(1)
                    await msg.channel.purge(limit = 3)
                    await sleep(1)
                    await msg.channel.send(f"{msg.author.mention} has used a banned word")
    async def command_log(client, ctx, cmd_name):
        embed = discord.Embed(
            title = "SleepBot Command Logs",
            description = ("Command: {}\nMessage Content: {}".format(cmd_name, ctx.message.content)),
            colour = random.randint(0, 0xffffff)
        )
        embed.add_field(name = "In Guild:", value = "{}".format(ctx.guild), inline = False)
        embed.add_field(name = "In Channel:", value = "{} Channel_ID: {}".format(ctx.channel, ctx.channel.id), inline = False)
        embed.add_field(name = "Author:", value = "{}, Nick: {}, ID: {}".format(ctx.author, ctx.author.nick, ctx.author.id), inline = False)
        embed.add_field(name = "Time:", value = "{}".format(datetime.now()), inline = False)

        await client.get_channel('869507682455920640').send(embed = embed)
                      
    #lockdown cmd
    @commands.command(aliases=['br','restrict'],help ='Bot Restrict - this is a permamant deal which makes members mentioned not allowed to use the bot anymore (under contruction)') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    @commands.check(sec)
    async def botrestrict(ctx,member : discord.Member):
        a = ctx.member.id
        print(a)
        br.append(a)
        await ctx.send()

def setup(client):
    client.add_cog(Mod(client))



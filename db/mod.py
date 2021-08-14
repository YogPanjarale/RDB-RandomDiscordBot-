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
filtered_words = pd.read_csv('/home/pi/rdb/r/db/swears.txt')['swears'].to_list()
fw = ['mg.s','m.sp']
br = []
def br(ctx)->bool:
    if ctx.author.id in br:
        return True
    else:
        return False
        
class Mod(commands.Cog):

    @commands.command(aliases=['del','d','rem'],help='delete messages command')
    @commands.check(sec)
    async def delete(self,ctx,term : int = ''):
        delete = discord.Embed(title = '',description=f'messages deleted = {term}')
        await ctx.channel.purge(limit=term+1)
        await ctx.send(embed = delete,delete_after=0.1)
    @commands.Cog.listener()
    async def on_message(self,msg):
        if not msg.author.bot:
            for word in filtered_words:
                if word in msg.content:
                    await sleep(1)
                    await msg.channel.purge(limit = 3)
                    await sleep(1)
                    await msg.channel.send(f"{msg.author.mention} has used a banned word")
 
    #lockdown cmd
    @commands.command(aliases=['br','restrict'],help ='Bot Restrict - this is a permamant deal which makes members mentioned not allowed to use the bot anymore (under contruction)') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    @commands.check(sec)
    async def botrestrict(ctx,member : discord.Member):
        a = ctx.member.id
        print(a)
        br.append(a)
        await ctx.send('you cant use the bot , sorry')

def setup(client):
    client.add_cog(Mod(client))



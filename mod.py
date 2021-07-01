import discord
from main import mgsec, sec
from discord import member
from discord import channel
from discord.ext import commands ,tasks
from discord.ext.commands import Context, context
from discord import Member
from better_profanity import Profanity
from discord.guild import Guild
from discord.message import Message
import numpy
import pandas as pd
import json
import os
from asyncio import sleep
filtered_words = pd.read_csv('swears.txt')['swears'].to_list()
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
        g:discord.Guild=msg.guild
        role=discord.utils.get(g.roles,name='ld')
        if not msg.author.bot:
            for word in filtered_words:
                if word in msg.content:
                    await sleep(1)
                    await msg.channel.purge(limit = 3)
                    await msg.author.add_roles(role)
                    await sleep(1)
                    await msg.channel.send(f"{msg.author.mention} has used a banned word")
                    
                    
       
    #lockdown cmd
    @commands.command('br')
    @commands.check(sec)
    async def br(ctx,member : discord.Member):
        a = ctx.member.id
        print(a)
        br.append(a)
        await ctx.send()
    @commands.command('ld')
    @commands.has_permissions(kick_members = True)
    async def ld(self,ctx,member : discord.Member):
        g:discord.Guild=ctx.guild
        lockdown = discord.utils.get(g.roles,name='ld')
        await member.add_roles(lockdown)
        await ctx.send(member.mention+" is going thru a temporary lockdown")

    #remove lockdown

    @commands.command('rld')
    @commands.has_permissions(kick_members = True)
    async def rld(self,ctx,member : discord.Member):
        g:discord.Guild=ctx.guild
        rlockdown = discord.utils.get(g.roles,name='ld')
        await member.remove_roles(rlockdown)
        await ctx.send(member.mention+" the lockdown is over , sorry for the inconvenience")

def setup(client):
    client.add_cog(Mod(client))



import discord
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
from time import sleep
filtered_words = pd.read_csv('swears.txt')['swears'].to_list()
fw = ['mg.s','m.sp']
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
                    sleep(1)
                    await msg.channel.purge(limit = 3)
                    await msg.author.add_roles(role)
                    await msg.channel.send(f"{msg.author.mention} has used a banned word , sending them to lockdown")
                    
                    
       
    #lockdown cmd

    @commands.command('ld')
    @commands.has_permissions(kick_members = True)
    async def ld(self,ctx,member : discord.Member):
        lockdown = ctx.guild.get_role(839409585706237973)
        await member.add_roles(lockdown)
        await ctx.send(member.mention+" is going thru a temporary lockdown")

    #remove lockdown

    @commands.command('rld')
    @commands.has_permissions(kick_members = True)
    async def rld(self,ctx,member : discord.Member):
        rlockdown = ctx.guild.get_role(839409585706237973)
        await member.remove_roles(rlockdown)
        await ctx.send(member.mention+" the lockdown is over , sorry for the inconvenience")

def setup(client):
    client.add_cog(Mod(client))



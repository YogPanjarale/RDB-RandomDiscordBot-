from logging import exception
import discord
from main import mgsec, sec
from discord import member 
import mysql.connector as m
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
br = []
def br(ctx):
    if ctx.author.id in br:
        return True
    else:
        return False
        
class Mod(commands.Cog):

    @commands.command(aliases=['del','d','rem'],help='delete messages command')
    @commands.check(mgsec)
    async def delete(self,ctx,term : int = ''):
        delete = discord.Embed(title = '',description=f'messages deleted = {term}')
        await ctx.channel.purge(limit=term+1)
        await ctx.send(embed = delete,delete_after=0.1)
 
    #lockdown cmd
    @commands.command(aliases=['br','restrict'],help ='Bot Restrict - this is a permament deal which makes members mentioned not allowed to use the bot anymore (under contruction)') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    @commands.check(sec)
    async def botrestrict(ctx,member:discord.Member):
        member=member
        cur = m.connect(host='localhost',database='mgsb',user='MG',password='mg@123')
        game = cur.cursor()
        users = '''insert into admin(name,nameid) values("%s","%s");'''
        a = ctx.member.id
        b = ctx.member.name
        params = a,b
        await ctx.send("user has been restricted to bot use")
        game.execute(users%params)
        game.close()

    @commands.command(aliases=['roles','role'],help="Get the amount of members that have a particular role")
    @commands.cooldown(1,1,commands.BucketType.guild)
    @commands.check(sec)    
    async def r(self,ctx,role:discord.Role):               
        b=len([m for m in ctx.guild.members if role in m.roles])
        await ctx.send(f"Number of members that have the role are {b}")

def setup(client):
    client.add_cog(Mod(client))



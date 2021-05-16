import discord
from discord import member
from discord.ext import commands ,tasks
from discord.ext.commands import Context, context
from discord import Member
from better_profanity import Profanity
from discord.guild import Guild
from discord.message import Message
import pandas as pd

filtered_words = pd.read_csv('swears.txt')['swears'].to_list()


class Mod(commands.Cog):
           
    @commands.Cog.listener()
    async def on_message(self,msg:Message):
        g:Guild=msg.guild
        role=g.get_role(839409585706237973)
        if not msg.author.bot:
            for word in filtered_words:
                if word in msg.content:
                    await msg.channel.send(f"{msg.author.mention} has used a banned word , sending them to lockdown")
                    await msg.author.add_roles(role)
                    return await msg.delete()

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



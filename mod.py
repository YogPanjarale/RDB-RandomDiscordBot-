import discord
from discord.ext import commands ,tasks
from discord.ext.commands import Context
from discord import Member
from profanity_filter import ProfanityFilter
import spacy
nlp = spacy.load('en_core_web_sm')
pf = ProfanityFilter()
class Mod(commands.Cog):
    @commands.Cog.listener()

    async def on_message(self,msg):
        r= pf.censor(msg.content)
        if r != msg.content:
            await msg.delete()
        # await msg.edit(content = r)

    #clear messages acc to amt
    @commands.command('d')
    @commands.has_permissions(manage_messages = True)
    async def d(self,ctx,amount=10):
        await ctx.channel.purge(limit = amount)

    #kick members
    @commands.command('k')
    @commands.has_permissions(kick_members = True)
    async def k(self,ctx,member : discord.Member,*,reason = "no reason provided"):
        await member.send("you have been kicked from the server, Because:"+reason)
        await member.kick(reason = reason)

def setup(client):
    client.add_cog(Mod(client))



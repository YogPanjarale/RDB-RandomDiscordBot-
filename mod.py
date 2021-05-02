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
        myEmbed = discord.Embed(title = 'messages deleted succesfully',description='msgs = '+amount-1)
        await ctx.message.reply(embed=myEmbed)
    #kick members
    @commands.command('k')
    @commands.has_permissions(kick_members = True)
    async def k(self,ctx,member : discord.Member,*,reason = "no reason provided"):
        await member.send("you have been kicked from the server,because: "+reason)
        await member.kick(reason = reason)

    #ban members
    @commands.command('b')
    @commands.has_permissions(ban_members = True)
    async def b(self,ctx,member : discord.Member,*,reason = "no reason provided"):
        await member.send("you have been banned from the server,because: "+reason)
        await member.ban(reason = reason)

def setup(client):
    client.add_cog(Mod(client))



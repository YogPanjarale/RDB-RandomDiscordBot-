import discord
from discord.ext import commands ,tasks
from discord.ext.commands import Context
from discord import Member

class mod(commands.Cog):

    filtered_words = ["nibba","nibbi","bc","ass","bitch","fuck"]

    @commands.Cog.listener()

    async def on_message(msg):
        for word in filtered_words:
            if word in msg.content:
                await msg.delete()

        await commands.process_commands(msg)

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
    client.add_cog(mod(client))
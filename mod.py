import discord
from discord.ext import commands ,tasks
from discord.ext.commands import Context
from discord import Member

class Mod(commands.Cog):
    #clear messages acc to amt
    @commands.command('d')
    @commands.has_permissions(manage_messages = True)
    async def d(self,ctx,amount=0):
        await ctx.channel.purge(limit = amount+1)
        myEmbed = discord.Embed(title = 'messages deleted succesfully - ',description=amount)
        myEmbed.set_footer(text="asked By ".title(
            )+str(ctx.author), icon_url=str(ctx.message.author.avatar_url))
        await ctx.message.channel.send(embed=myEmbed,delete_after = 2)
    
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
    
    #delete channels
    @commands.command('dc')
    @commands.has_permissions(manage_channels = True)
    async def dc(self,ctx,channel : discord.TextChannel):
        await ctx.send("the channel was deleted succesfully")
        await channel.delete()


def setup(client):
    client.add_cog(Mod(client))



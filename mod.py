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
    
    #clear messages acc to amt
    
    @commands.command('d')
    @commands.has_permissions(manage_messages = True)
    async def d(self,ctx,amount=0):
        await ctx.channel.purge(limit = amount+1)
        myEmbed = discord.Embed(title = 'messages deleted succesfully - ',description=amount)
        myEmbed.set_footer(text="asked By ".title(
            )+str(ctx.author), icon_url=str(ctx.message.author.avatar_url))
        await ctx.message.channel.send(embed=myEmbed,delete_after = 1)

           
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
        


    #kick members
    
    @commands.command('k')
    @commands.has_permissions(kick_members = True)
    async def k(self,ctx,member : discord.Member,*,reason = "no reason provided"):
        
        await member.kick(reason = reason)
    
    #ban members
    
    @commands.command('b')
    @commands.has_permissions(ban_members = True)
    async def b(self,ctx,member : discord.Member,*,reason = "no reason provided"):
        await member.send("you have been banned from the server,because: "+reason)
        await member.ban(reason = reason)
    
    #unban members
    
    @commands.command('ub')
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx,*,member):
        banned_users = await ctx.guild.bans()
        member_name , member_disc = member.split('#')
        for banned_entry in banned_users:
            user = banned_entry.user
            if(user.name,user.discriminator)==(member_name,member_disc):
                await ctx.guild.unban(user)
                await ctx.send(member_name+" has been succesfully unbanned")
                return

        await ctx.send(member+" was not found")

    #delete channels
    
    @commands.command('dc')
    @commands.has_permissions(manage_channels = True)
    async def dc(self,ctx,channel : discord.TextChannel):
        await ctx.send("the channel was deleted succesfully")
        await channel.delete()
    
    #mute members

    @commands.command('m')
    @commands.has_permissions(kick_members = True)
    async def m(self,ctx,member : discord.Member):
        muted_role = ctx.guild.get_role(839003264992935947)
        await member.add_roles(muted_role)
        await ctx.send(member.mention+" has been muted")

    #unmute members

    @commands.command('um')
    @commands.has_permissions(kick_members = True)
    async def m(self,ctx,member : discord.Member):
        muted_role = ctx.guild.get_role(839003264992935947)
        await member.remove_roles(muted_role)
        await ctx.send(member.mention+" has been unmuted")

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



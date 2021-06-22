from discord.ext.commands.errors import BotMissingPermissions, CommandInvokeError, CommandNotFound
from my_utils.my_cc import addCC, getAllCC, searchCC, searchCCByUser
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands.context import Context
from discord import Embed

class CC(commands.Cog):
    def __init__(self, bot):
        self.bot:Bot     = bot
    @commands.command(name="cca")
    async def ccl(self,ctx:Context,user:str=""):
        serverId = ctx.message.guild.id
        if user =="":
            r = getAllCC(serverID=serverId)
            print(len(r))
            myEmbed = Embed(title=f"All Commands Created Since last reset ",description=f"Total of {len(r)} Commands")
            
            if len(r)==0:
                myEmbed.add_field(name="No Commands found for this server",value="______")
            elif len(r)>=1:
                j=0
                for i in r:
                    j+=1
                    des = i['description'] + "\n**Created At " + i['time_created']   +"**"
                    n=f"{j}."+ i["name"] 
                    myEmbed.add_field(name=n,value=des,inline=False)
            return await ctx.channel.send(embed = myEmbed)
        if user.startswith("<@"):
            name = user
            r = searchCCByUser(serverID=serverId,user=name.replace("!",""))
            if r:
                myEmbed = Embed(name=f"Commands Created By {name}",description=f"{name} has created {len(r)} Commands ")
                j=0
                for i in r:
                    j+=1
                    des = i['description'] + "\n**Created At " + i["time_created"]+"**"
                    n=f"{j}."+ i["name"] 
                    myEmbed.add_field(name=n,value=des,inline=False)
                return await ctx.channel.send(embed = myEmbed)
            else:
                myEmbed = Embed(name=f"Commands Created By {name}",description=f"{name} has not created any Commands")
                return await ctx.channel.send(embed = myEmbed)
            pass

    @commands.command(name="cc")
    async def cc(self,ctx:Context,name:str=" ",*description):
        serverId = ctx.message.guild.id        
        if name.startswith("<@"):
            r = searchCCByUser(serverID=serverId,user=name.replace("!",""))
            if r:
                myEmbed = Embed(name=f"Commands Created By {name}",description=f"{name} has created{len(r)+1} Commands ")
                for i in r:
                    des = i['description'] + "\n**Created At " + i["time_created"]+"**"
                    myEmbed.add_field(name=i["name"],value=des,inline=False)
                return await ctx.channel.send(embed = myEmbed)
            else:
                myEmbed = Embed(name=f"Commands Created By {name}",description=f"{name} has not created any Commands")
        if name == " ":
            return await ctx.channel.send("You did not provide the command name!")
        if not description :
            return await ctx.channel.send("You did not provide the command description!")
        if name in self.bot.all_commands:
            return await ctx.channel.send(f"{name} command already exists!")
        description=' '.join(description)
        addCC(serverID=serverId,name=name,description=description,user=ctx.author.mention)
        await ctx.channel.send(f"Command with name : `{name}` , and description : `{description}` has been added by {ctx.author.mention}")
    @commands.Cog.listener()
    async def on_command_error(self,ctx:Context,error):
        if isinstance(error, CommandNotFound):
            msg:str=ctx.message.content
            serverId = ctx.message.guild.id
            print(error)
            r=searchCC(serverID=serverId,name=msg[len(self.bot.command_prefix):])
            if r:
                return await ctx.channel.send(r['description'])
                
            return await ctx.channel.send("sorry , an error occured , contact Mg or Yog")
        elif isinstance(error,BotMissingPermissions) or isinstance(error,CommandInvokeError):
            raise error
        raise error
def setup(client):
    client.add_cog(CC(client))
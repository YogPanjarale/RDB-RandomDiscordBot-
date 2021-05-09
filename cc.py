from discord.ext.commands.errors import CommandNotFound
from my_utils.my_cc import addCC, getAllCC, searchCC, searchCCByUser
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands.context import Context
from discord import Embed

class CC(commands.Cog):
    def __init__(self, bot):
        self.bot:Bot     = bot
    @commands.command(name="ccl")
    async def ccl(self,ctx:Context,user:str=""):
        if user =="":
            r = getAllCC()
            if r:
                # print("====================")
                # print("r=")
                # print(r)
                # print("====================")
                myEmbed = Embed(name=f"All Commands Created Since last reset ",description=f"Total of {len(r)+1} Commands")
                for i in r:
                    # print("====================")
                    # print("i=")
                    # print(i)
                    # print("====================")
                    des = i['description'] + "\nC*reated At " + i["time-created"]+"*"
                    myEmbed.add_field(name=i["name"],value=des,inline=False)
                return await ctx.channel.send(embed = myEmbed)
        if user.startswith("<@"):
            name = user
            r = searchCCByUser(name.replace("!",""))
            if r:
                # print("====================")
                # print("r=")
                # print(r)
                # print("====================")
                myEmbed = Embed(name=f"Commands Created By {name}",description=f"{name} has created{len(r)+1} Commands ")
                for i in r:
                    # print("====================")
                    # print("i=")
                    # print(i)
                    # print("====================")
                    des = i['description'] + "\nC*reated At " + i["time-created"]+"*"
                    myEmbed.add_field(name=i["name"],value=des,inline=False)
                return await ctx.channel.send(embed = myEmbed)
            else:
                myEmbed = Embed(name=f"Commands Created By {name}",description=f"{name} has not created any Commands")
                return await ctx.channel.send(embed = myEmbed)
            pass

    @commands.command(name="cc")
    async def cc(self,ctx:Context,name:str=" ",*description):
        if name.startswith("<@"):
            r = searchCCByUser(name.replace("!",""))
            if r:
                # print("====================")
                # print("r=")
                # print(r)
                # print("====================")
                myEmbed = Embed(name=f"Commands Created By {name}",description=f"{name} has created{len(r)+1} Commands ")
                for i in r:
                    # print("====================")
                    # print("i=")
                    # print(i)
                    # print("====================")
                    des = i['description'] + "\nC*reated At " + i["time-created"]+"*"
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
        addCC(name=name,description=description,user=ctx.author.mention)
        await ctx.channel.send(f"Command with name : `{name}` , and description : `{description}` has been added by {ctx.author.mention}")
    @commands.Cog.listener()
    async def on_command_error(self,ctx:Context,error):
        if isinstance(error, CommandNotFound):
            msg:str=ctx.message.content
            
            r=searchCC(msg[len(self.bot.command_prefix):])
            # print(r)
            if r:
                return await ctx.channel.send(r['description'])
                
            return await ctx.channel.send("<:bruh:839886556667838484>")
        raise error
def setup(client):
    client.add_cog(CC(client))
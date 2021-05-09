from discord.ext.commands.errors import CommandNotFound
from my_utils.my_cc import addCC, searchCC, serchCCByUser
from discord.ext import commands
from discord.ext.commands.context import Context
from discord import Embed

class CC():
    @commands.command(name="cc")
    async def cc(self,ctx:Context,name:str=" ",*description):
        if name.startswith("<@"):
            r = serchCCByUser(name.replace("!",""))
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
     
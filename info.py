import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Info(commands.Cog):
    help='who,when,what and where'
    @commands.command(name='ver',help ='current version of the bot') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    async def ver(self, context):
        myEmbed = discord.Embed(
            title="Current Version", description="Version 1.8", color=0x00ff00)
        myEmbed.add_field(name="Version Code", value="v1.8.5", inline=False)
        myEmbed.add_field(name="Date Released",
                          value="March 29th ,2021", inline=False)
        await context.message.reply(embed=myEmbed)
    # info abt the bot

    @commands.command(name='who',help ='info about the bot and owners - part 1') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    async def who(self, context):

        myEmbed = discord.Embed(
            title="who am i", description=">>>About me", color=0x0000ff)
        myEmbed.add_field(
            name="name", value="the name given to me was 'MGs Search Bot' , MGSB for short ", inline=False)
        myEmbed.add_field(name="Created By",
                          value="**[Mg](https://github.com/omegamg05111101)** - **<@!518118892317442059>**", inline=False)
        myEmbed.add_field(name="Heavily Contributed by",
                          value="**[Yog](https://github.com/YogPanjarale)** - **<@!705463601011490907>**", inline=False)
        myEmbed.add_field(name="Languages used",
                          value="Python", inline=False)

        await context.message.reply(embed=myEmbed)

    #info

    @commands.command(name='info',help ='info about the bot and developers - part 2') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    async def info(self, context):

        myEmbed1 = discord.Embed(
            title="bot,docs and contributors", description=">>>About me part 2", color=0x0000ff)
        myEmbed1.add_field(name="Invite MGSB to your server - ",
                          value="[Invite Link](https://discord.com/oauth2/authorize?client_id=826067681111310426&scope=bot&permissions=470281334)", inline=False)
        myEmbed1.add_field(name="Created using - ",
                          value="[Discord.py](https://discordpy.readthedocs.io/en/stable)", inline=False)
        myEmbed1.add_field(name="DPY server - ",
                          value="[Discord.py - Discord server](https://discord.gg/dpy)", inline=False)
        myEmbed1.add_field(name="Contributers - ",
                          value="[ZeusAbhijeet](https://github.com/ZeusAbhijeet)", inline=False)
        myEmbed1.add_field(name="top.gg - ",
                          value="[Bot Profile](https://top.gg/bot/826067681111310426)", inline=False)
        await context.message.reply(embed=myEmbed1)

def setup(client):
    client.add_cog(Info(client))

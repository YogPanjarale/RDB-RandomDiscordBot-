import discord
from discord.ext import commands
from discord.ext.commands.context import Context


class Info(commands.Cog):
    @commands.command(name='ver')
    async def ver(self, context):
        myEmbed = discord.Embed(
            title="Current Version", description="Version 1.4", color=0x00ff00)
        myEmbed.add_field(name="Version Code", value="v1.4.1", inline=False)
        myEmbed.add_field(name="Date Released",
                          value="March 29th ,2021", inline=False)
        await context.message.reply(embed=myEmbed)
    # info abt the bot

    @commands.command(name='who')
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

    @commands.command(name='info')
    async def info(self, context):

        myEmbed1 = discord.Embed(
            title="bot,docs and contributors", description=">>>About me part 2", color=0x0000ff)
        myEmbed1.add_field(name="Created using - ",
                          value="[Discord.py](https://discordpy.readthedocs.io/en/stable)", inline=False)
        myEmbed1.add_field(name="DPY server - ",
                          value="[Discord.py - Discord server](https://discord.gg/dpy)", inline=False)
        myEmbed1.add_field(name="BOT Repo",
                          value="[MGSB Repo](https://github.com/YogPanjarale/RDB-RandomDiscordBot-)", inline=False)
        myEmbed1.add_field(name="Contributers - ",
                          value="[ZeusAbhijeet](https://github.com/ZeusAbhijeet) \n [its_charmandar](https://github.com/itsCharmander)", inline=False)

        await context.message.reply(embed=myEmbed1)

    
    # ping

    @commands.command('ping')
    async def ping(self, context):

        latency = self.client.latency * 1000
        myEmbed = discord.Embed(
            title="Ping", description=f'latency : {latency} ms', color=0x00ff00)

        await context.message.reply(embed=myEmbed)
    # help



def setup(client):
    client.add_cog(Info(client))

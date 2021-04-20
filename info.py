import discord
from discord.ext import commands
from discord.ext.commands.context import Context


class Info(commands.Cog):
    @commands.command(name='ver')
    async def ver(self, context):
        myEmbed1 = discord.Embed(
            title="Current Version", description="Version 1.0", color=0x00ff00)
        myEmbed1.add_field(name="Version Code", value="v1.1.0", inline=False)
        myEmbed1.add_field(name="Date Released",
                           value="March 29th ,2021", inline=False)
        await context.message.reply(embed=myEmbed1)
    # info abt the bot

    @commands.command(name='who')
    async def who(self, context):

        myEmbed2 = discord.Embed(
            title="who am i", description=">>>About me", color=0x0000ff)
        myEmbed2.add_field(
            name="name", value="the name given to me was 'MGs Search Bot' , MGSB for short ", inline=False)
        myEmbed2.add_field(name="Created By",
                           value="Mg (Mg#9916)", inline=False)
        myEmbed2.add_field(name="Languages used",
                           value="Python only", inline=False)

        await context.message.reply(embed=myEmbed2)
    # ping

    @commands.command('ping')
    async def ping(self, context):

        latency = self.client.latency * 1000
        myEmbed11 = discord.Embed(
            title="Ping", description=f'latency : {latency} ms', color=0x00ff00)

        await context.message.reply(embed=myEmbed11)
    # help

    @commands.command(name='mg')
    async def mg(context):

        myEmbed4 = discord.Embed(
            title="mgsb help commands", description="these r the primary cmds", color=0x00ff00)
        myEmbed4.add_field(name="1) mg - ",
                           value="brings up this page", inline=True)
        myEmbed4.add_field(name="2) who - ",
                           value="tells you about the bot", inline=True)
        myEmbed4.add_field(
            name="3) cmd - ", value="shows u all the search commands that u can use", inline=True)
        myEmbed4.add_field(
            name="4) ver - ", value="tells you about the current version of the bot", inline=True)
        myEmbed4.add_field(name="5) sad - ", value="fun cmd1", inline=True)
        myEmbed4.add_field(name="6) how - ", value="fun cmd2", inline=True)
        myEmbed4.add_field(name="7) say - ", value="fun cmd3", inline=True)
        myEmbed4.add_field(name="8) ping - ",
                           value="know your latency", inline=True)

        await context.message.reply(embed=myEmbed4)


def setup(client):
    client.add_cog(Info(client))

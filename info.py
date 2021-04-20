import discord
from discord.ext import commands
from discord.ext.commands.context import Context


class Info(commands.Cog):
    @commands.command(name='ver')
    async def ver(self, context):
        myEmbed = discord.Embed(
            title="Current Version", description="Version 1.0", color=0x00ff00)
        myEmbed.add_field(name="Version Code", value="v1.1.0", inline=False)
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
                           value="Mg (Mg#9916)", inline=False)
        myEmbed.add_field(name="Languages used",
                           value="Python only", inline=False)

        await context.message.reply(embed=myEmbed)
    # ping

    @commands.command('ping')
    async def ping(self, context):

        latency = self.client.latency * 1000
        myEmbed = discord.Embed(
            title="Ping", description=f'latency : {latency} ms', color=0x00ff00)

        await context.message.reply(embed=myEmbed)
    # help

    @commands.command(name='mg')
    async def mg(context):

        myEmbed = discord.Embed(
            title="mgsb help commands", description="these r the primary cmds", color=0x00ff00)
        myEmbed.add_field(name="1) mg - ",
                           value="brings up this page", inline=True)
        myEmbed.add_field(name="2) who - ",
                           value="tells you about the bot", inline=True)
        myEmbed.add_field(
            name="3) cmd - ", value="shows u all the search commands that u can use", inline=True)
        myEmbed.add_field(
            name="4) ver - ", value="tells you about the current version of the bot", inline=True)
        myEmbed.add_field(name="5) sad - ", value="fun cmd1", inline=True)
        myEmbed.add_field(name="6) how - ", value="fun cmd2", inline=True)
        myEmbed.add_field(name="7) say - ", value="fun cmd3", inline=True)
        myEmbed.add_field(name="8) ping - ",
                           value="know your latency", inline=True)

        await context.message.reply(embed=myEmbed)


def setup(client):
    client.add_cog(Info(client))

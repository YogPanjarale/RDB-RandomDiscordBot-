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
        myEmbed.add_field(name="Made By",
                          value="Yog @.Yog#7840", inline=False)
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



def setup(client):
    client.add_cog(Info(client))

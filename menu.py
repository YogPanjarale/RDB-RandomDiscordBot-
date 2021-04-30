import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.member import Member


class menu(commands.Cog):
    @commands.command(name='mg2')
    async def mg(self, context):

        myEmbed = discord.Embed(
            title="mgsb help commands", description="these r the primary cmds,dont forget to put prefix mg. before each of them", color=0x00ff00)
        myEmbed.add_field(name="1) mg - ",
                          value="brings up this help page", inline=True)
        myEmbed.add_field(name="2) util - ", value="Utility cmds", inline=True)
        myEmbed.add_field(name="3) fun - ", value="Fun cmds", inline=True)
        myEmbed.add_field(
            name="4) cmd - ", value="shows u all the search commands that u can use", inline=True)

        await context.message.reply(embed=myEmbed)

    @commands.command(name='util')
    async def util(self, context):

        myEmbed = discord.Embed(
            title="Utility Commands", description="these r one of the secondary cmds,dont forget to put prefix mg. before each of them", color=0x00ff00)
        myEmbed.add_field(
            name="1) ver - ", value="tells u about the current version of the bot", inline=True)
        myEmbed.add_field(name="2) who - ",
                          value="tells u about the bot and founders", inline=True)
        myEmbed.add_field(name="3) ping - ",
                          value="know your latency with this command", inline=True)
        myEmbed.add_field(name="4) addnews/news - ",
                          value="make the bot remember important milestones and news that recently happend in the server", inline=True)

        await context.message.reply(embed=myEmbed)

    @commands.command(name='fun')
    async def fun(self, context):

        myEmbed = discord.Embed(
            title="Fun commands", description="these r one of the secondary cmds,dont forget to put prefix mg. before each of them", color=0x00ff00)
        myEmbed.add_field(name="1) sad - ", value="fun cmd1", inline=True)
        myEmbed.add_field(name="2) hello - ", value="fun cmd2", inline=True)
        myEmbed.add_field(name="3) say - ", value="fun cmd3", inline=True)
        myEmbed.add_field(name="4) how - ", value="fun cmd4", inline=True)
        myEmbed.add_field(name="5) pfp - ", value="fun cmd5", inline=True)
        myEmbed.add_field(name="6) fight - ", value="fun cmd6", inline=True)

        await context.message.reply(embed=myEmbed)


def setup(client):
    client.add_cog(menu(client))

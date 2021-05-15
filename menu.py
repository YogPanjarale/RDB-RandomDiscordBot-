import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.member import Member


class menu(commands.Cog):
    @commands.command(name='mg')
    async def mg(self, context):

        myEmbed = discord.Embed(
            title="mgsb help commands", description="these r the primary cmds,dont forget to put the prefix before each of them", color=0x00ff00)
        myEmbed.add_field(name="1) mg - ",
                          value="brings up this help page", inline=True)
        myEmbed.add_field(name="2) utils - ", value="Utility cmds", inline=True)
        myEmbed.add_field(name="3) fun - ", value="Fun cmds", inline=True)
        myEmbed.add_field(
            name="4) cmd - ", value="shows u all the search commands that u can use", inline=True)
        myEmbed.add_field(
            name="5) mod - ", value="Creator and Moderation commands", inline=True)
        await context.message.reply(embed=myEmbed)

    @commands.command(name='utils')
    async def utils(self, context):

        myEmbed = discord.Embed(
            title="Utility Commands", description="these r one of the secondary cmds,dont forget to put the prefix before each of them", color=0x00ff00)
        myEmbed.add_field(
            name="1) ver - ", value="tells u about the current version of the bot", inline=True)
        myEmbed.add_field(name="2) who - ",
                          value="tells u about the bot and founders", inline=True)
        myEmbed.add_field(name="3) info - ",
                          value="dpy server , contributers , and dpy docs", inline=True)
        myEmbed.add_field(name="4) ping - ",
                          value="know your latency with this command", inline=True)
        myEmbed.add_field(name="5) addnews/news - ",
                          value="make the bot remember important milestones and news that recently happend in the server", inline=True)

        await context.message.reply(embed=myEmbed)

    @commands.command(name='mod')
    async def util(self, context):

        myEmbed = discord.Embed(
            title="Creator and moderation commands", description="these r one of the secondary cmds,dont forget to put the prefix before each of them", color=0x00ff00)
        myEmbed.add_field(
            name="1) re - ", value="reloads the files , re fun/mod/cmd/menu/info", inline=True)
        myEmbed.add_field(name="2) m/um - ",
                          value="mutes or unmutes someone", inline=True)
        myEmbed.add_field(name="3) k - ",
                          value="kicks someone", inline=True)
        myEmbed.add_field(name="4) d - ",
                          value="deletes a specific amount of msgs", inline=True)
        myEmbed.add_field(name="5) b/ub - ",
                          value="bans or unbans someone", inline=True)
        myEmbed.add_field(name="6) ld/rld - ",
                          value="puts a person in lockdown , i.e , they cant see or text messages in any channel of the server", inline=True)
        myEmbed.add_field(name="7) dc - ",
                          value="deletes a specific channel of the server - use carefully", inline=True)


        await context.message.reply(embed=myEmbed)

    @commands.command(name='fun')
    async def fun(self, context):

        myEmbed = discord.Embed(
            title="Fun commands", description="these r one of the secondary cmds,dont forget to put the prefix before each of them", color=0x00ff00)
        myEmbed.add_field(name="1) hello - ", value="fun cmd1", inline=True)
        myEmbed.add_field(name="2) say - ", value="fun cmd2", inline=True)
        myEmbed.add_field(name="3) how - ", value="fun cmd3", inline=True)
        myEmbed.add_field(name="4) pfp - ", value="fun cmd4", inline=True)
        myEmbed.add_field(name="5) 8b - ", value="fun cmd6", inline=True)
        myEmbed.add_field(name="6) spam - ", value="fun cmd7", inline=True)
        myEmbed.add_field(name="7) count - ", value="fun cmd8", inline=True)
        myEmbed.add_field(name="8) custom command (cc) - ", value="fun cmd9", inline=True)

        await context.message.reply(embed=myEmbed)


def setup(client):
    client.add_cog(menu(client))

from dotenv import main
from main import bot_name 
import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.member import Member


class menu(commands.Cog):
    @commands.has_permissions(ban_members=True)
    @commands.command(name = 'mg')
    async def mg(self,ctx):
        mge = discord.Embed(title='MGSB Bot setup',description='to setup MGSB in your server , do the following steps - ')
        mge.add_field(name = "1) ld role -",value="create a role called 'ld' where the role can't view see any channels (text, voice or even stage) , the perm to view channel should be crossed out in the channel settings")
        mge.add_field(name = "2) Appeal channel - ",value="this should be the only channel that the ld role can view and text in , also , dont allow everyone to view this channel")
        mge.add_field(name = "3) mm role - ",value="create a role called 'mm', this will be used for people who shouldnt be allowed to use the bot")
        mge.add_field(name = '4) Main cmd - ',value = "Use this command to bring up the main menu , it contains 5 commands that bring up the sub-menus")
        await ctx.send(embed=mge)
    @commands.command(name='main')
    async def mai(self, context):

        myEmbed = discord.Embed(
            title=f"{bot_name} help commands", description="these r the primary cmds,dont forget to put the prefix before each of them", color=0x00ff00)
        myEmbed.add_field(name="1) main - ",
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
        myEmbed.add_field(name="4) addnews/news - ",
                          value="make the bot remember important milestones and news that recently happend in the server", inline=True)

        await context.message.reply(embed=myEmbed)

    @commands.command(name='mod')
    async def util(self, context):

        myEmbed = discord.Embed(
            title="Creator and moderation commands", description="these r one of the secondary cmds,dont forget to put the prefix before each of them", color=0x00ff00)
        myEmbed.add_field(
            name="1) re - ", value="reloads the files , re fun/mod/cmd/menu/info", inline=True)
        myEmbed.add_field(name="2) ld/rld - ",
                          value="puts a person in lockdown , i.e , they cant see or text messages in any channel of the server", inline=True)



        await context.message.reply(embed=myEmbed)

    @commands.command(name='fun')
    async def fun(self, context):

        myEmbed = discord.Embed(
            title="Fun commands", description="these r one of the secondary cmds,dont forget to put the prefix before each of them", color=0x00ff00)
        myEmbed.add_field(name="1) hello/sus/bruh/hifi - ", value="fun gif cmds", inline=True)
        myEmbed.add_field(name="2) say - ", value="repeat cmd", inline=True)
        myEmbed.add_field(name="3) how - ", value="how are you", inline=True)
        myEmbed.add_field(name="4) pfp - ", value="view the pfps of members", inline=True)
        myEmbed.add_field(name="5) 8b - ", value="ask the 8ball a Q", inline=True)
        myEmbed.add_field(name="6) spam - ", value="spam a message - not for members", inline=True)
        myEmbed.add_field(name="7) count - ", value="make the bot do a countdown", inline=True)
        myEmbed.add_field(name="8) custom command (cc) - ", value="create special message commands of your own", inline=True)

        await context.message.reply(embed=myEmbed)


def setup(client):
    client.add_cog(menu(client))

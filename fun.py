import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.member import Member


class Fun(commands.Cog):

    @commands.command(name='how')
    async def how(self, ctx):

        myEmbed = discord.Embed(
            title="how am i?", description="im doing great , thank u for asking :))", color=0x00ff00)
        myEmbed.add_field(name="what about you sir/ma'am?",
                           value="how are u today ?", inline=False)
        myEmbed.set_image(
            url="https://media.giphy.com/media/Xfbugf2U4rC1Db4NSq/giphy.gif")

        await ctx.message.reply(embed=myEmbed)
    # pfp

    @commands.command('pfp')
    async def pfp(self, ctx, member: Member = None):
        if not member:
            member = ctx.author

        await ctx.send.reply(member.avatar_url)

    @commands.command(name='say')
    async def say(self, ctx, *, term: str = ''):

        await ctx.message.reply(term)

    @commands.command(name='hello')
    async def hello(self, ctx):

        myEmbed = discord.Embed(
            title="",
            color=discord.Colour.purple()
        )
        myEmbed.set_image(
            url="https://media.giphy.com/media/djRJNZqj508sE/giphy.gif")

        await ctx.message.reply(embed=myEmbed)

    @commands.command('sad')
    async def sad(self, ctx):
        myEmbed = discord.Embed(
            title="sad?", description="dont be , ur bots here for you ", color=0x00ff00)
        myEmbed.add_field(name="what caused it?",
                          value="r u actually crying or crying internally?", inline=False)
        myEmbed.add_field(name="friends or family?",
                          value="doesnt matter , go vibe to some music!!", inline=False)

        await ctx.message.reply(embed=myEmbed)


def setup(client):
    client.add_cog(Fun(client))

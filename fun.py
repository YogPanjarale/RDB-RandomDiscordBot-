import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.member import Member


class Fun(commands.Cog):

    @commands.command(name='how')
    async def how(context):

        myEmbed6 = discord.Embed(
            title="how am i?", description="im doing great , thank u for asking :))", color=0x00ff00)
        myEmbed6.add_field(name="what about you sir/ma'am?",
                           value="how are u today ?", inline=False)

        await context.message.reply(embed=myEmbed6)
    # pfp

    @commands.command('pfp')
    async def pfp(ctx, member: Member = None):
        if not member:
            member = ctx.author

    @commands.command(name='say')
    async def say(ctx, *, term: str = ''):

        await ctx.message.reply(term)

    @commands.command('sad')
    async def sad(context):

        myEmbed1 = discord.Embed(
            title="sad?", description="dont be , ur bots here for you ", color=0x00ff00)
        myEmbed1.add_field(
            name="what caused it?", value="r u actually crying or crying internally?", inline=False)
        myEmbed1.add_field(name="friends or family?",
                           value="doesnt matter , go vibe to some music!!", inline=False)

        await context.message.reply(embed=myEmbed1)


def setup(client):
    client.add_cog(Fun(client))

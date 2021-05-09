import discord
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands.context import Context
from discord.member import Member
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot:Bot     = bot      
    @commands.command(name="count")
    async def count(self,ctx:Context,n:str):
        if n.isnumeric():
            for i in range(int(n)):
                await ctx.channel.send(str(i+1))
        else:
            await ctx.channel.send("Not a valid number to count")
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

        await ctx.send(member.avatar_url)

    @commands.command(name='say')
    async def say(self, ctx, *, term: str = ''):

        await ctx.message.reply(term)

    @commands.command(name='hello')
    async def hello(self, ctx):
        hellogifs = ["https://media.giphy.com/media/djRJNZqj508sE/giphy.gif",
        "https://giphy.com/gifs/mW05nwEyXLP0Y",
        "https://giphy.com/gifs/hello-adam-demamp-television-6yU7IF9L3950A",
        "https://giphy.com/gifs/hello-hi-dzaUX7CAG0Ihi"]
        myEmbed = discord.Embed(
            title="",
            color=discord.Colour.purple()
        )
        myEmbed.set_image(
            url=random.choice(hellogifs))

        await ctx.message.reply(embed=myEmbed)
         
    @commands.has_role('mgsb admin')
    @commands.command('spam')
    async def spam(self,ctx:Context,n:str='',*terms):
        term =''
        if not( n.isnumeric()):
            await ctx.channel.send("You did not provide the number")
            term+=n
            n=1
        for t in terms:
            term+=' '+str(t)
        n:int=int(n)
        for i in range(n):
            # await ctx.channel.send(f"{int(n)-i} remain")
            await ctx.channel.send(term)
        #8ball cmd

    @commands.command(name='8b', help='Replies to a question')
    async def eightball(self, ctx, *, question):
        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt.',
                     'Yes - definitely.',
                     'You may rely on it.',
                     'As I see it, yes.',
                     'Most likely.',
                     'Outlook good.',
                     'Yes.',
                     'Signs point to yes.',
                     'Reply hazy, try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     "Don't count on it.",
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Very doubtful.']
        embed1=discord.Embed(title=f'8ball', 
            description=f'Get your questions answered by 8ball',
            colour=discord.Colour.red())
        embed1.add_field(name=f'Question:', value=f'{question}')
        embed1.add_field(name=f'Answer:', value=f'{random.choice(responses)}')
        embed1.set_footer(text=f'Requested by {ctx.author}')
        await ctx.send(embed=embed1)   


def setup(client):
    client.add_cog(Fun(client))

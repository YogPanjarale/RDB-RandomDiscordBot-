import discord
from discord.ext import commands 
from discord.ext.commands.bot import Bot
from discord.ext.commands.context import Context
from discord.ext.commands.errors import CommandInvokeError, CommandNotFound, MissingPermissions
from discord.member import Member
import random
from discord.message import Message 

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot:Bot  = bot
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
        myEmbed.add_field(name="what about you ?",
                           value="how are u today ?", inline=False)
        myEmbed.set_image(
            url="https://media.giphy.com/media/Zd5ZqNSI0mfymBRNQc/giphy.gif")

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

    @commands.command(name='e')
    async def e(self,ctx,*, term:str='',targetMember : discord.Member = None):
        if targetMember == None:
            targetMember = ctx.message.author
        y=term.lower()
        l=list(y)
        random.shuffle(l)
        c = ''.join(l)
        f=''
        a=['a','c','e','g','i','k','m','o','q','s','u','w','y']
        b=['b','d','f','h','j','l','n','p','r','t','v','x','z']
        for i in c:
            if i in a:
                f+="I"
            elif i in b:
                f+="l"
            elif i==" ":
                f+=i
        myEmbed11=discord.Embed(title="Encrypter", description="lithium Encryption",color=0x992d22)
        myEmbed11.add_field(name="Encrypt", value=term,inline=False)
        myEmbed11.add_field(name="Encrypted as", value=f,inline=False)
        await targetMember.send(embed = myEmbed11)

    @commands.command(name='hi')
    async def hi(self, ctx):
        hellogifs = ["https://media.giphy.com/media/djRJNZqj508sE/giphy.gif",
        "https://media.giphy.com/media/Vbtc9VG51NtzT1Qnv1/giphy.gif",
        "https://media.giphy.com/media/dzaUX7CAG0Ihi/giphy.gif",
        "https://media.giphy.com/media/mW05nwEyXLP0Y/giphy.gif"]
        myEmbed = discord.Embed(
            title="",
            color=discord.Colour.purple()
        )
        myEmbed.set_image(
            url=random.choice(hellogifs))

        await ctx.message.reply(embed=myEmbed)

    @commands.command(name='hifi')
    async def hifi(self, ctx):
        hifigifs = ["https://media.giphy.com/media/bp0fLZr8kFz4Bm4kRV/giphy.gif",
        "https://media.giphy.com/media/HX3lSnGXZnaWk/giphy.gif",
        "https://media.giphy.com/media/DuWay0MoeQxWM/giphy.gif",
        "https://media.giphy.com/media/3o7TKWuJdNJSt2JHpK/giphy.gif"]
        myEmbed1 = discord.Embed(
            title="",
            color=discord.Colour.purple()
        )
        myEmbed1.set_image(
            url=random.choice(hifigifs))

        await ctx.message.reply(embed=myEmbed1)

    @commands.command(name='sus')
    async def sus(self, ctx):
        susgifs = ["https://media.giphy.com/media/cJMlR1SsCSkUjVY3iK/giphy.gif",
        "https://media.giphy.com/media/TPl5N4Ci49ZQY/giphy.gif",
        "https://media.giphy.com/media/kaq6GnxDlJaBq/giphy.gif"]
        myEmbed = discord.Embed(
            title="",
            color=discord.Colour.purple()
        )
        myEmbed.set_image(
            url=random.choice(susgifs))

        await ctx.message.reply(embed=myEmbed)       

    @commands.command(name='bruh')
    async def bruh(self, ctx):
        bruhgifs = ["https://media.giphy.com/media/VIOkcgpsnA2Zy/giphy.gif",
        "https://media.giphy.com/media/kWp8QC99Z6xFn8bF0v/giphy.gif",
        "https://media.giphy.com/media/fm0FiSOfefH5m/giphy.gif",
        "https://media.giphy.com/media/CxQw7Rc4Fx4OBNBLa8/giphy.gif"]
        myEmbed = discord.Embed(
            title="",
            color=discord.Colour.purple()
        )
        myEmbed.set_image(
            url=random.choice(bruhgifs))

        await ctx.message.reply(embed=myEmbed)

    
    
    @commands.command(name = 's')
    async def sp(self, ctx, *, term: str = '',member:discord.Member = None):
        member = ctx.author
        spoiler=discord.Embed(title="**SPOILER**\n\n", description=f"\n||{member.mention} has put a spoiler :-||\n\n||{term}||",color=discord.Colour.blue())
        await ctx.send(embed = spoiler)

    #@commands.command(name = 'hw')
    #async def hw(self,ctx,)

    
    @commands.command('whoismg')
    async def whoismg(self,ctx):
        wimg = ["cant say , he could be lying abt his name for all yk" , 'dont ask a man his salary , a woman her age and mg his name' ,'he\'ll reveal that on his bday , i.e if u remember it' , 'even yog , the co founder of mgsb doesnt know','stop asking that','not telling','shoo','idk okay?','why do u wanna know?','hint : its related to a gods name','do i look like google to u?' , '>:((','smh','bruh stop already with this Q','dont ask']
        hdp = random.choice(wimg)
        wmg = discord.Embed(name = '',description=hdp)
        await ctx.send(embed = wmg)


    @commands.command("nick",pass_context=True)
    @commands.has_permissions(manage_nicknames=True)
    async def chnick(self,ctx, member: discord.Member, nick):
        await member.edit(nick=nick)
        await ctx.send(f'Nickname was changed for {member.mention} ')

        
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

    @commands.command(name='8b')
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

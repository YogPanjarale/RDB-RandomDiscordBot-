import discord
from discord.ext import commands 
from discord.ext.commands.bot import Bot
from discord.ext.commands.context import Context
from discord.ext.commands.errors import CommandInvokeError, CommandNotFound, MissingPermissions
from discord.member import Member
import random
from discord.message import Message 
from time import sleep

class Fun(commands.Cog):
    help='Fun commands'
    def __init__(self, bot):
        self.bot:Bot  = bot
    @commands.command(aliases=['count','c','countdown'],help ='make the bot do a countdown using this command') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    async def coun(self,ctx:Context,n:str):
        if n.isnumeric():
            for i in range(int(n)):
                await ctx.channel.send(str(i+1))
        else:
            await ctx.channel.send("Not a valid number to count")
    # pfp
    @commands.command(aliases=['pfp','dp','photo'],help ='view the members profile image') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    async def pf(self, ctx, member: Member = None):
        if not member:
            member = ctx.author

        await ctx.send(member.avatar_url)



    @commands.command(aliases=['say','repeat','talk'],help ='make the bot repeat after you for extra emphasis or validation') 
    @commands.cooldown(1,20,commands.BucketType.guild)

    async def sa(self, ctx, *, term: str = ''):
        await ctx.message.reply(term)

    @commands.command(aliases=['encrypt','e','enc'],help ='use this command to create passwords with lithium encryption , the bot sends u the messaage privately') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    async def en(self,ctx,*, term:str=''):
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

    @commands.command(aliases=['hello','hey','hi'],help ='hello gifs') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    async def hit(self, ctx,member:discord.Member):
        if member==None:
            member==ctx.message.author
        hellogifs = ["https://media.giphy.com/media/djRJNZqj508sE/giphy.gif",
        "https://media.giphy.com/media/Vbtc9VG51NtzT1Qnv1/giphy.gif",
        "https://media.giphy.com/media/dzaUX7CAG0Ihi/giphy.gif",
        "https://media.giphy.com/media/mW05nwEyXLP0Y/giphy.gif"]
        myEmbed = discord.Embed(
            title=f"{ctx.message.author.name} is saying hello to {member.name}",
            color=discord.Colour.purple()
        )
        myEmbed.set_image(
            url=random.choice(hellogifs))

        await ctx.message.reply(embed=myEmbed)

    @commands.command(aliases=['highfive','h5','high5'],help ='high five gifs') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    async def hifi(self, ctx,member:discord.Member):
        if member==None:
            member==ctx.message.author
        hifigifs = ["https://media.giphy.com/media/bp0fLZr8kFz4Bm4kRV/giphy.gif",
        "https://media.giphy.com/media/HX3lSnGXZnaWk/giphy.gif",
        "https://media.giphy.com/media/DuWay0MoeQxWM/giphy.gif",
        "https://media.giphy.com/media/3o7TKWuJdNJSt2JHpK/giphy.gif"]
        myEmbed1 = discord.Embed(
            title=f"{ctx.message.author.name} is giving a high five to {member.name}",
            color=discord.Colour.purple()
        )
        myEmbed1.set_image(
            url=random.choice(hifigifs))

        await ctx.message.reply(embed=myEmbed1)

    @commands.command(aliases=['suspicious','sus','susy'],help ='') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    async def sussy(self, ctx):
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

    @commands.command(aliases=['bruh','bro','bruhh'],help ='') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    async def bruhhh(self, ctx):
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

    
    
    @commands.command(aliases=['s','spoiler','hide'],help ='spoiler command - replaces your message with a spoiler') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    async def sp(self, ctx, *, term: str = ''):
        member = ctx.author
        spoiler=discord.Embed(title="**SPOILER**\n\n", description=f"\n{member.mention} has put a spoiler :-\n\n||{term}||",color=discord.Colour.blue())
        await ctx.channel.purge(limit=1)
        sleep(1)
        await ctx.send(embed = spoiler)

    
    @commands.command(aliases=['whoismg'],help ='who is the creator of this bot? - use this to find out') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    async def whotfismg(self,ctx):
        wimg = ["cant say , he could be lying abt his name for all yk" , 'dont ask a man his salary , a woman her age and mg his name' ,'he\'ll reveal that on his bday , i.e if u remember it' , 'even yog , the co founder of mgsb doesnt know','stop asking that','not telling','shoo','idk okay?','why do u wanna know?','hint : its related to a gods name','do i look like google to u?' , '>:((','smh','bruh stop already with this Q','dont ask']
        hdp = random.choice(wimg)
        wmg = discord.Embed(name = '',description=hdp)
        await ctx.send(embed = wmg)


    @commands.command(aliases=['nick','cnick','chnick'],pass_context=True,help ="change nicknames of members - requires 'manage messages' permission") 
    @commands.cooldown(1,20,commands.BucketType.guild)
    @commands.has_permissions(manage_nicknames=True)
    async def changenick(self,ctx, member: discord.Member, nick):
        await member.edit(nick=nick)
        await ctx.send(f'Nickname was changed for {member.mention} ')


    @commands.command(aliases=['8b','askbot','askme'],help ='ask the bot important life questions - (the ones that can be answered with yes and no , hes not einstien)') 
    @commands.cooldown(1,20,commands.BucketType.guild)
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
        embed1=discord.Embed(title=f'AskBot', 
            description=f'Get your questions answered by the bot',
            colour=discord.Colour.red())
        embed1.add_field(name=f'Question:', value=f'{question}')
        embed1.add_field(name=f'Answer:', value=f'{random.choice(responses)}')
        embed1.set_footer(text=f'Requested by {ctx.author}')
        await ctx.send(embed=embed1)   




def setup(client):
    client.add_cog(Fun(client))

from os import name
import w as wolframalpha
from main import bot_prefix,owak,waak
from mod import br
import math
from my_utils.get_covid_data import getCovidData
from my_utils.my_youtube_search import YoutubeResult, searchYT
import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from dpymenus import Page, PaginatedMenu
import requests
from googlesearch import search
from urllib.parse import quote
from time import sleep

class Cmd(commands.Cog):

    help='search commands'
    @commands.command(aliases=['cov','corona'],help ='command used to see current covid status in india') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    async def covid(self,ctx:Context,*,term:str=""):
        r = getCovidData()
        if "india" in term:
            r = getCovidData("india")
        myEmbed = discord.Embed(title="Covid 19 - World data")
        myEmbed.add_field(name="Total Cases",value=r.cases)
        myEmbed.add_field(name="Total Active",value=r.active)
        myEmbed.add_field(name="Total Recovered",value=r.recovered)
        myEmbed.add_field(name="Total Deaths",value=r.deaths)
        await ctx.message.channel.send(embed=myEmbed)

    @commands.command(aliases=["w"],help='know the current weather of your city using this')
    @commands.cooldown(1,5,commands.BucketType.guild)
    async def weather(self,ctx,*,city:str=''):
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={owak}'
        response = requests.get(url).json()
        x=response['main']
        a = x['temp']
        temp = math.floor((a-273))
        statement1=response['weather'][1]['main']
        statement2 = response['weather'][1]['description']
        mt=x['feels_like']
        mintemp=math.floor((mt-273))
        p=x['pressure']
        pressure = math.floor((p//100))
        humidity = x['humidity']
        visibility=response['visibility']
        wind = response['wind']['speed']
        weather = discord.Embed(title='Weather',description=f'weather report for city : {city}')
        weather.add_field(name='Temperature (Celsius)',value =temp,inline=True)
        weather.add_field(name='Pressure (Pascals)',value =pressure,inline=True)
        weather.add_field(name='Humidity (%)',value =humidity,inline=True)
        weather.add_field(name='Feels Like',value =mintemp,inline=True)
        weather.add_field(name='Visibility (metres)',value =visibility,inline=True)
        weather.add_field(name='Wind (m/s)',value =wind,inline=True)
        weather.add_field(name='Weather statement',value =statement1+statement2,inline=True)
        await ctx.send(embed=weather)

    @commands.command(aliases=["wa"],help='know the answer to any math question using this command')
    @commands.cooldown(1,10,commands.BucketType.guild)
    async def answer(self,ctx,*,term:str=''):

        question = term

        app_id = waak

        client = wolframalpha.Client(app_id)

        ans = client.ask(f"{question}")
        
        answer = discord.Embed(title="WolframAlpha answers",description='Get your questions answered using WolframAlpha')
        answer.add_field(name='Answer',value=ans)
        await ctx.send(embed=answer)

    @commands.command(aliases=['git','gh'],help ='github profile command - view profiles') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    async def github(self, ctx: Context, *, term: str = ''):
        r = requests.get(f'https://api.github.com/users/{term}').json()
        try:
            myEmbed = discord.Embed(
                title=term.title(), description=r['bio'], url=r['html_url'])
            myEmbed.add_field(name="Public repos", value=r['public_repos'])
            myEmbed.add_field(name="Public gists", value=r['public_gists'])
            myEmbed.add_field(name="Followers", value=r['followers'])
            myEmbed.add_field(name="Following", value=r['following'])
            myEmbed.set_thumbnail(url=r['avatar_url'])
            myEmbed.set_footer(text="asked By ".title(
            )+str(ctx.author), icon_url=str(ctx.message.author.avatar_url))
            await ctx.message.channel.send(embed=myEmbed)
        except Exception as e:
            myEmbed = discord.Embed(
                title="Not Found !", description="I cound not find that user")
            await ctx.message.channel.send(embed=myEmbed)
    @commands.command(aliases=['google','g'],help ='google search command - provides upto 10 results along with redirect link') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    async def ggl(self, ctx, *, term: str = ''):
        l = search(term,num_results=10,lang='en',proxy=None)  
        b = str(l).replace("'",'') 
        c = str(b).replace('[','')
        d = str(c).replace(']','')
        f = str(d).replace(',','\n')
        g = str(f).replace("/search",'https://google.com/search')
        j = str(term).replace(" ",'+') 
        myEmbed1 = discord.Embed(title = ':mag: **Here\'s what i found** :mag:', description = g)
        myEmbed1.add_field(name= '**For more results** - ' , value = f'[Browser redirect Link](https://www.google.com/search?q={j})')
        await ctx.send(embed = myEmbed1)

    @commands.command(aliases=['youtube','ytsearch'],help ='youtube search command - paginated results') 
    @commands.cooldown(1,20,commands.BucketType.guild)

    async def yt(self, ctx, *, term: str = ''):
        l = searchYT(term)
        # print(l)
        l = l[:5]

        menu = PaginatedMenu(ctx)
        i: YoutubeResult
        pages = []
        for i in l:
            # embed = discord.Embed( )
            # embed.set_thumbnail(url=i.thumbnail[0])
            # embed.add_field(name="Views",value=i.views)
            page = Page(
                title=i.title[0], description=i.description[0], color=0x00ff00, url=i.url[0])
            page.set_thumbnail(url=i.thumbnail[0])
            page.add_field(name="Views", value=i.views,inline=True)
            page.add_field(name="duration", value=i.duration,inline=True)
            page.add_field(name="channel", value=i.channel,inline=True)
            page.add_field(name="publish time", value=i.publish_time,inline=True)
            pages.append(page)
            # await ctx.message.channel.send(embed=embed)
        menu.add_pages(pages)
        menu.show_command_message()
        await menu.open()
    # 
    @commands.command(aliases=['updates'],help ='upcoming updates') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    async def uu(self, context):

        myEmbed3 = discord.Embed(
            title="Upcoming Updates", description=">>>these r the upcoming updates , coming as update 1.5 ", color=0xff0000)
        myEmbed3.add_field(
            name="spotify cmd", value="searches for info abt a specific song", inline=True)
        myEmbed3.add_field(
            name="fb", value="searches for a particular acc on facebook", inline=True)
        myEmbed3.add_field(
            name="ps", value="searches for a specific game or application on the google playstore", inline=True)
        myEmbed3.add_field(
            name="amzn", value="searches for a specific item on amazon", inline=True)

        await context.message.reply(embed=myEmbed3)

def setup(client):
    client.add_cog(Cmd(client))

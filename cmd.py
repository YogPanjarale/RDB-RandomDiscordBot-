from main import bot_prefix
from my_utils.get_covid_data import getCovidData
from my_utils.my_youtube_search import YoutubeResult, searchYT
import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from googlesearch import search
from dpymenus import Page, PaginatedMenu
import requests
from googlesearch.googlesearch import GoogleSearch, SearchResponse, SearchResult
from urllib.parse import quote
import instatools3

class Cmd(commands.Cog):

    @commands.command('cov')
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

    @commands.command('git')
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
    @commands.command('ggl')
    async def ggl(self, ctx, *, term: str = ''):

        
        for i in search(term, tld="com", num=5, stop=10, pause=2):
            
            myEmbed1 = discord.Embed()
            msg = await ctx.send(embed=myEmbed1)
            myEmbed1.add_field(name = '**Here\'s what i found**', description = i)
            await msg.edit(embed = myEmbed1)

    @commands.command('insta')
    async def insta(self, ctx, *, term: str = ''):
        u = instatools3.igstalker(term)
        if u:
            print(u)
            follower = u['follower']
            following = u['following']
            bio = u['bio']
            if bio == '':
                bio = '__'
            username = u['username']
            pictureUrl = u['pic']
            profilelink = f'https://instagram.com/{username}'
            print(pictureUrl)
            myEmbed = discord.Embed(
                title="IG acc search", description=">>>this is what i found", color=0x00ff00)
            # myEmbed.set_image(pictureUrl)
            myEmbed.add_field(name="name of account : ",
                              value=username, inline=False)
            myEmbed.add_field(name="no. of followers : ",
                              value=follower, inline=False)
            myEmbed.add_field(name="following : ",
                              value=following, inline=False)
            myEmbed.add_field(name="bio : ", value=bio, inline=False)
            myEmbed.add_field(name="link to profile : ",
                              value=profilelink, inline=False)

            await ctx.message.channel.send(embed=myEmbed)

        if not u:
            myEmbed8 = discord.Embed(
                title="IG acc search", description="IG acc not found :(( ,retry", color=0x00ff00)

            await ctx.message.channel.send(embed=myEmbed8)

    @commands.command('yt')
    async def youtube(self, ctx, *, term: str = ''):
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
            page.set_image(url=i.thumbnail[0])
            page.add_field(name="Views", value=i.views)
            page.add_field(name="duration", value=i.duration)
            page.add_field(name="channel", value=i.channel)
            page.add_field(name="publish time", value=i.publish_time)
            pages.append(page)
            # await ctx.message.channel.send(embed=embed)
        menu.add_pages(pages)
        menu.show_command_message()
        await menu.open()
    # commands to use

    @commands.command(name='cmd')
    async def cmd(self, context):

        myEmbed3 = discord.Embed(
            title="Help", description=f">>>these r the search commands , all require u to use prefix '{bot_prefix}' to search", color=0xff0000)
        myEmbed3.add_field(
            name="insta", value="searches for a particular instagram acc\n(under construction)", inline=True)
        #myEmbed3.add_field(
            #name="fb", value="searches for a particular acc on facebook", inline=True)
        myEmbed3.add_field(
            name="ggl", value="searches for a specific topic on the google search engine\n(under construction)", inline=True)
        myEmbed3.add_field(
            name="wikp", value="searches for a specific topic on wikipedia\n(under construction)", inline=True)
        myEmbed3.add_field(
            name="git", value="searches for a specific user on github", inline=True)
        myEmbed3.add_field(
            name="yt", value="searches for a specific video on youtube", inline=True)
        #myEmbed3.add_field(
            #name="spotify", value="searches for a specific song on spotify", inline=True)
        #myEmbed3.add_field(
            #name="amzn", value="searches for a specific item on amazon", inline=True)
        #myEmbed3.add_field(
            #name="ps", value="searches for a specific application/game on the google playstore", inline=True)
        myEmbed3.add_field(
            name="twit", value="searches for a particular twitter acc\n(under construction) ", inline=True)

        await context.message.reply(embed=myEmbed3)
    
    @commands.command(name='uu')
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
    @commands.command(name="corona")
    async def corona(self,ctx:Context):
        await ctx.channel.send("WIP")

def setup(client):
    client.add_cog(Cmd(client))

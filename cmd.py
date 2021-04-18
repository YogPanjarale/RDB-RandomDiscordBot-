import discord
from discord.ext import commands
from discord.ext.commands.context import Context

import requests
from googlesearch.googlesearch import GoogleSearch, SearchResponse,SearchResult
from urllib.parse import quote
import instatools3
from utils.youtube_search import search


class Cmd(commands.Cog):
    @commands.command('gh')
    async def github(self,ctx:Context,*,term:str=''):
        r  = requests.get(f'https://api.github.com/users/{term}').json()
        try:
            myEmbed=discord.Embed(title=term.title(),description=r['bio'],url=r['html_url'])
            myEmbed.add_field(name="Public repos",value=r['public_repos'])
            myEmbed.add_field(name="Public gists",value=r['public_gists'])
            myEmbed.add_field(name="Followers",value=r['followers'])
            myEmbed.add_field(name="Following",value=r['following'])
            myEmbed.set_thumbnail(url=r['avatar_url'])
            myEmbed.set_footer(text="asked By ".title()+str(ctx.author),icon_url=str(ctx.message.author.avatar_url))
            await ctx.message.channel.send(embed=myEmbed)
        except Exception as e:
            myEmbed= discord.Embed(title="Not Found !",description="I cound not find that user")
            await ctx.message.channel.send(embed=myEmbed)
    @commands.command('ggl')
    async def ggl(self,ctx, *, term: str=''):
        # result = search(query=term,num_results=10)
        result:SearchResponse = GoogleSearch().search(query= term,num_results=5)
        print(term)
        myEmbed = discord.Embed(title="Google search", description=">>>this is     what i found",color=0x00ff00,url='https://google.com/?q='+quote(term))
        #myEmbed.set_image(pictureUrl)
        r:SearchResult
        for r in result.results:
            myEmbed.add_field(name=r.title,inline=False,value=r.url)
        if len(result.results)<=0:
            myEmbed.set_footer(text="Nothing Found from the search")
        await ctx.message.channel.send(embed=myEmbed)
    @commands.command('insta')
    async def insta(self,ctx, *, term: str = ''):
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
            myEmbed.add_field(name="following : ", value=following, inline=False)
            myEmbed.add_field(name="bio : ", value=bio, inline=False)
            myEmbed.add_field(name="link to profile : ",
                            value=profilelink, inline=False)

            await ctx.message.channel.send(embed=myEmbed)

        if not u:
            myEmbed8 = discord.Embed(
                title="IG acc search", description="IG acc not found :(( ,retry", color=0x00ff00)

            await ctx.message.channel.send(embed=myEmbed8)
    @commands.command('yt')
    async def youtube(self,ctx,*,term:str = ''):
        myEmbed = discord.Embed()
def setup(client):
    client.add_cog(Cmd(client))
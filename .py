from discord import embeds
from discord.ext.commands.core import command
import instatools3

from discord.ext.commands import Bot, Context
from gsearch.googlesearch import search
from googlesearch.googlesearch import GoogleSearch, SearchResponse, SearchResult
from urllib.parse import quote
import discord
import requests
from requests.models import Response
client = Bot('!')
client.load_extension('cmd')


@client.command('insta')
async def insta(ctx, *, term: str = ''):
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
        myEmbed7 = discord.Embed(
            title="IG acc search", description=">>>this is what i found", color=0x00ff00)
        # myEmbed7.set_image(pictureUrl)
        myEmbed7.add_field(name="name of account : ",
                           value=username, inline=False)
        myEmbed7.add_field(name="no. of followers : ",
                           value=follower, inline=False)
        myEmbed7.add_field(name="following : ", value=following, inline=False)
        myEmbed7.add_field(name="bio : ", value=bio, inline=False)
        myEmbed7.add_field(name="link to profile : ",
                           value=profilelink, inline=False)

        await ctx.message.channel.send(embed=myEmbed7)

    if not u:
        myEmbed8 = discord.Embed(
            title="IG acc search", description="IG acc not found :(( ,retry", color=0x00ff00)

        await ctx.message.channel.send(embed=myEmbed8)
# except Exception as e:
#     print("An exception occurred: ", e)


print('Bot Ready')
client.run('Nzg2MDY1MzM0Mjg0NTgyOTIy.X9A-ZA.gATX7E4OjH93tlq-Ph5Ye4-WYIU')

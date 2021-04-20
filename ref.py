#importing packages

# import discord
# from discord.ext import commands ,tasks
# import instatools3
# from googlesearch.googlesearch import GoogleSearch,SearchResponse,SearchResult
# from discord import Member
# from urllib.parse import quote , ParseResult
# from itertools import cycle
# import requests
# from googleapiclient.discovery import build

#client(bot)
this_is="done"
# client = commands.Bot(command_prefix='mg.')
# status = cycle(['mg','mg.'])
#version of bot
  
# @client.command(name='ver')

# async def ver(context):
    
#     myEmbed1 = discord.Embed(title="Current Version", description="Version 1.0",color=0x00ff00)
#     myEmbed1.add_field(name="Version Code", value="v1.0.8",inline=False)
#     myEmbed1.add_field(name="Date Released", value="March 29th ,2021",inline=False)
    
#     await context.message.reply(embed=myEmbed1)
    
# @client.command(name='sad')

# async def sad(context):
    
#     myEmbed1 = discord.Embed(title="sad?", description="dont be , ur bots here for you ",color=0x00ff00)
#     myEmbed1.add_field(name="what caused it?", value="r u actually crying or crying internally?",inline=False)
#     myEmbed1.add_field(name="friends or family?", value="doesnt matter , go vibe to some music!!",inline=False)
    
#     await context.message.reply(embed=myEmbed1)

#  #info abt the bot
     
# @client.command(name='who')

# async def who(context):
    
#     myEmbed2 = discord.Embed(title="who am i", description=">>>About me",color=0x0000ff)
#     myEmbed2.add_field(name="name", value="the name given to me was 'MGs Search Bot' , MGSB for short ",inline=False)
#     myEmbed2.add_field(name="Created By", value="Mg (Mg#9916)",inline=False)
#     myEmbed2.add_field(name="Languages used", value="Python only",inline=False)
    
#     await context.message.reply(embed=myEmbed2)
   
# #help

# @client.command(name='mg')

# async def mg(context):
    
#     myEmbed4 = discord.Embed(title="mgsb help commands", description="these r the primary cmds",color=0x00ff00)
#     myEmbed4.add_field(name="1) mg - ", value="brings up this page",inline=True)
#     myEmbed4.add_field(name="2) who - ", value="tells you about the bot",inline=True)
#     myEmbed4.add_field(name="3) cmd - ", value="shows u all the search commands that u can use",inline=True) 
#     myEmbed4.add_field(name="4) ver - ", value="tells you about the current version of the bot",inline=True)
#     myEmbed4.add_field(name="5) sad - ", value="fun cmd1",inline=True)
#     myEmbed4.add_field(name="6) how - ", value="fun cmd2",inline=True)
#     myEmbed4.add_field(name="7) say - ", value="fun cmd3",inline=True)
#     myEmbed4.add_field(name="8) ping - ", value="know your latency",inline=True)
    
#     await context.message.reply(embed=myEmbed4)


# #commands to use 
   
# @client.command(name='cmd')

# async def cmd(context):
    
#     myEmbed3 = discord.Embed(title="Help", description=">>>these r the search commands , all require u to use prefix 'mg.' to search",color=0xff0000)
#     myEmbed3.add_field(name="insta", value="searches for a particular instagram acc",inline=True)
#     myEmbed3.add_field(name="fb", value="searches for a particular acc on facebook",inline=True)
#     myEmbed3.add_field(name="ggl", value="searches for a specific topic on the google search engine",inline=True)
#     myEmbed3.add_field(name="wikp", value="searches for a specific topic on wikipedia",inline=True)
#     myEmbed3.add_field(name="git", value="searches for a specific topic on github",inline=True)
#     myEmbed3.add_field(name="yt", value="searches for a specific video on youtube",inline=True)
#     myEmbed3.add_field(name="spotify", value="searches for a specific song on spotify",inline=True)
#     myEmbed3.add_field(name="amzn", value="searches for a specific item on amazon",inline=True)
#     myEmbed3.add_field(name="fk", value="searches for a specific item on flipkart",inline=True)
#     myEmbed3.add_field(name="ps", value="searches for a specific application/game on the google playstore",inline=True)
#     myEmbed3.add_field(name="twit", value="searches for a particular twitter acc",inline=True)
    
#     await context.message.reply(embed=myEmbed3)


#repeat function

# @client.command(name='say')
# async def say(ctx, *, term: str=''):
    
#   await ctx.message.reply(term)
  
# #github function 

# @client.command('git')
# async def git(ctx,*,term:str=''):
#     r  = requests.get(f'https://api.github.com/users/{term}').json()
#     try:
#         myEmbed10=discord.Embed(title=term.title(),description=r['bio'],url=r['html_url'])
#         myEmbed10.add_field(name="Public repos",value=r['public_repos'])
#         myEmbed10.add_field(name="Public gists",value=r['public_gists'])
#         myEmbed10.add_field(name="Followers",value=r['followers'])
#         myEmbed10.add_field(name="Following",value=r['following'])
#         myEmbed10.set_thumbnail(url=r['avatar_url'])
#         myEmbed10.set_footer(text="asked By ".title()+str(ctx.author),icon_url=str(ctx.message.author.avatar_url))
#         await ctx.message.reply(embed=myEmbed10)
#     except Exception as e:
#         myEmbed10= discord.Embed(title="Not Found !",description="I cound not find that user")
#         await ctx.message.reply(embed=myEmbed10)
            
#how are you 

# @client.command(name='how')

# async def how(context):
    
#     myEmbed6 = discord.Embed(title="how am i?", description="im doing great , thank u for asking :))",color=0x00ff00)
#     myEmbed6.add_field(name="what about you sir/ma'am?",value="how are u today ?",inline=False)

#     await context.message.reply(embed=myEmbed6)

# #yt search

# def get_service():
#     # Get developer key from "credentials" tab of api dashboard
#     return build("youtube", "v3", developerKey="AIzaSyDAxqV42_AkrQW_c4YyWanpBkrKZrNB-A4")

# def search(term, channel):
#     service = get_service()
#     resp = service.search().list(
#         part="id",
#         q=term,
#         safeSearch="none" if channel.is_nsfw() else "moderate",
#         videoDimension="2d",
#     ).execute()
#     return resp["items"][0]["id"]["videoId"]
   
#ggl search

# @client.command('ggl')
# async def ggl(ctx, *, term: str=''):
#     # result = search(query=term,num_results=3)
#     result:SearchResponse = GoogleSearch().search(query= term,num_results=3)
#     myEmbed9 = discord.Embed(title="Google search", description=">>>this is what i found",color=0x00ff00)
#     #myEmbed7.set_image(pictureUrl)
#     r:SearchResult
#     for r in result.results:
#         myEmbed9.add_field(name=r.title,inline=True,value=r.url)
#     if len(result.results)<=0:
#         myEmbed9.set_footer(text="Nothing Found from the search")
        
#     await ctx.message.reply(embed=myEmbed9)

# # #ping

# @client.command('ping')

# async def ping(context):
    
#     latency = round(client.latency,1)
#     myEmbed11 = discord.Embed(title="Ping", description=f'latency : {latency}',color=0x00ff00)

#     await context.message.reply(embed=myEmbed11)
    
  

#pfp

# @client.command('pfp')
# async def pfp(ctx, member: Member = None):
#  if not member:
#   member = ctx.author
  
#  await ctx.send(member.avatar_url)
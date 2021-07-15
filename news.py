from logging import addLevelName
from discord.ext.commands.context import Context
from my_utils.my_news import NewsObject, addNews, getAllNews
from discord.ext import commands
from dpymenus import Page, PaginatedMenu


class News(commands.Cog):
    help='inbuilt starboard'
    @commands.command(name='news',help ='this is the inbuilt starboard feature of the bot , use this command to view all the news and milestones done so far in the server') 
    @commands.cooldown(1,20,commands.BucketType.guild)
    async def getNews(self,ctx):
        result = getAllNews()
        menu = PaginatedMenu(ctx)
        pages=[]
        # item = 
        n =2
        r = [result[i:i+n] for i in range(0, len(result), n)]
        # print(r)
        for p in range(len(r)):
            items = r[p]
            page = Page(title=f"Page {p+1} of {len(r)}")
            # page = Page()
            for item in items:
                page.add_field(name = item.title,value=item.description,inline=False)
                page.add_field(name="Added By",value=item.added_by)
                page.add_field(name="Time Created",value=item.time_created)
            pages.append(page)
        menu.add_pages(pages)
        menu.show_command_message()
        menu.set_timeout(20)
        await menu.open()
    # TODO: add hint use `;` as seperator
    @commands.command(name='an',help ="this command is used to add news - use ';' between the name and description , this command requires members to staff") 
    @commands.has_permissions(ban_members=True,manage_roles=True)
    @commands.cooldown(1,20,commands.BucketType.guild)
    async def addNews(self,ctx:Context,*text):
        text:str = " ".join(text)
        title:str = text.split(';')[0]
        description:str = text.split(';',1)[1]
        author:str = str(ctx.author.mention)
        news = addNews(NewsObject(title=title,description=description,added_by=author))
        await ctx.channel.send(f"news with title : `{title}` and description : `{ description}` added by {author}")




def setup(client):
    client.add_cog(News(client))
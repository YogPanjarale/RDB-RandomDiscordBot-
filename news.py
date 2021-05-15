from my_utils.my_news import getAllNews
from discord.ext import commands
from dpymenus import Page, PaginatedMenu


class News(commands.Cog):
    @commands.command("news")
    async def getNews(self,ctx):
        r = getAllNews()
        menu = PaginatedMenu(ctx)
        pages=[]
        for i in r:
            page = Page(title = i.title,description=i.description)
            page.add_field(name="Time Created",value=i.time_created)
            page.add_field(name="Added By",value=i.added_by)
            pages.append(page)
        menu.add_pages(pages)
        menu.show_command_message()
        await menu.open()
        



def setup(client):
    client.add_cog(News(client))
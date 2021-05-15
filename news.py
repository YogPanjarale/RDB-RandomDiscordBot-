from my_utils.my_news import getAllNews
from discord.ext import commands
from dpymenus import Page, PaginatedMenu


class News(commands.Cog):
    @commands.command("news")
    async def getNews(self,ctx):
        r = getAllNews()
        menu = PaginatedMenu(ctx)
        pages=[]
        for i in range(r):
            item = r[i]
            page = Page(title = item.title,description=item.description)
            page.add_field(name="Time Created",value=item.time_created)
            page.add_field(name="Added By",value=item.added_by)
            pages.append(page)
        menu.add_pages(pages)
        menu.show_command_message()
        await menu.open()
        



def setup(client):
    client.add_cog(News(client))
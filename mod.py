import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from profanity_filter import ProfanityFilter
import spacy
nlp = spacy.load('en_core_web_sm')
pf = ProfanityFilter()
class Mod(commands.Cog):
    @commands.Cog.listener()

    async def on_message(self,msg):
        r= pf.censor(msg.content)
        if r != msg.content:
            await msg.delete()
        # await msg.edit(content = r)


def setup(client):
    client.add_cog(Mod(client))


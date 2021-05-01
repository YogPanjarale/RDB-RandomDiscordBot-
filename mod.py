import discord
from discord.ext import commands
from discord.ext.commands.context import Context
class Mod(commands.Cog):
    @commands.Cog.listener()

    async def on_message(self,msg):
        await msg.delete()


def setup(client):
    client.add_cog(Mod(client))


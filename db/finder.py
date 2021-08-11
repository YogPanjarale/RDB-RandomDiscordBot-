import discord
from discord.ext import commands 
from discord.ext.commands.bot import Bot
from discord.ext.commands.context import Context
from discord.ext.commands.errors import CommandInvokeError, CommandNotFound, MissingPermissions
from discord.member import Member
import random
from discord.message import Message 
from asyncio import sleep
import random as r
import mysql.connector as m
from Game2functions import *

class Finder(commands.Cog):

    @commands.command(aliases=['player','playername'],help ='use this command to see who all plays this game') 
    @commands.cooldown(1,10,commands.BucketType.user)
    async def players(self, ctx):
        cur = m.connect(host='localhost',database='mgsb',user='MG',password='mg@123')
        game = cur.cursor()
        tables = '''select name from player;'''
        game.execute(tables)
        l = game.fetchall()
        a = list(l)
        b = str(a).replace("[","")
        c=str(b).replace(']','')
        d = str(c).replace(',','')
        e=str(d).replace("'","")
        f=str(e).replace('(',"")
        g = str(f).replace(')','')
        game.close()
        print(g)
        players = discord.Embed(title='Current Players',description=g)
        await ctx.send(embed=players)

    @commands.command(aliases=['newuser','make'],help ='create an account for this game') 
    @commands.cooldown(1,10,commands.BucketType.guild)
    async def nuser(self, ctx):
        cur = m.connect(host='localhost',database='mgsb',user='MG',password='mg@123')
        game = cur.cursor()
        name=ctx.author.id
        create(name)
        game.close()
        await ctx.send(f"Player {ctx.author.name} with nameid = {name} has been created")

    @commands.command(aliases=['find','scavenge'],help ='explore the map to find items') 
    @commands.cooldown(1,10,commands.BucketType.user)
    async def explore(self, ctx, *, place: str = ''):
        cur = m.connect(host='localhost',database='mgsb',user='MG',password='mg@123')
        place = place.lower()
        animals = ['bear','monkey','narwhal','dodo','eagle','shark','bull','dragon','panthera','wolf']
        animalask=['army unit','pet']
        if place =='forest':
            number=25
            resource='logs'
            aa = r.randint(1,number)
            await ctx.send(f'you just got {aa} {resource} while exploring {place}')
            add(f'{ctx.author.id}',0,0,0,0,0,aa,0)
        elif place =='caves':
            #aa=explore(2,'metal(s)','caves')
            number=2
            resource='metals'
            aa = r.randint(1,number)
            await ctx.send(f'you just got {aa} {resource} while exploring {place}')
            add(f'{ctx.author.id}',0,0,0,0,0,0,aa)
        elif place =='savannah':
            #abc = explore(1,'animal(s)','savannah')
            abc= r.choice(animals)
            number=2
            aa = r.randint(1,number)
            aaa =r.choice(animalask)
            await ctx.send(f'you just found {aa} {abc} while exploring {place}')
            if aaa=='pet':
                add(f'{ctx.author.id}',0,0,0,aa,0,0,0)
                await ctx.send(f"{abc} has been added as a pet")
            else:
                add(f'{ctx.author.id}',0,0,aa,0,0,0,0)
                await ctx.send(f"{abc} has been added as an army unit")
        elif place=='tunnels':
            #aa = explore(10,'coins','tunnels')
            number=10
            resource='coins'
            aa = r.randint(1,number)
            await ctx.send(f'you just got {aa} {resource} while exploring {place}')
            add(f'{ctx.author.id}',aa,0,0,0,0,0,0)
        elif place=='plantations':
            #aa = explore(2,'fruit(s)','plantations')
            number=2
            resource='fruits'
            aa = r.randint(1,number)
            await ctx.send(f'you just got {aa} {resource} while exploring {place}')
            add(f'{ctx.author.id}',0,0,0,0,aa,0,0)
        elif place=='loot':
            a=r.randint(1,10)
            if a==1:
                await ctx.send("Your luck seems nice , u just got some cash while exploring a random loot box and old taverns")
                add(f'{ctx.author.id}',0,2,0,0,0,0,0)
            else:
                await ctx.send("sorry , this loot box seems to be empty , better luck next time")
        #else:
            #await ctx.send("sorry , you're not a registered member")

    @commands.command(aliases=['balance','items'],help ='check your balance and items that you have') 
    @commands.cooldown(1,10,commands.BucketType.guild)
    async def bal(self, ctx,member: Member = None):
        cur = m.connect(host='localhost',database='mgsb',user='MG',password='mg@123')
        game = cur.cursor()
        users = '''select coins,cash,army,pets,food,logs,metals from player where name ="%s"'''
        if not member:
            s = ctx.author.id
        else:
            s=member.id
        game.execute(users%s)
        l = game.fetchone()
        b = str(l).replace("[","")
        c=str(b).replace(']','')
        d = str(c).replace(',','')
        e=str(d).replace("'","")
        f=str(e).replace('(',"")
        g = str(f).replace(')','')      
        game.close()
        h=g.split(" ")
        coins = h[0]
        cash=h[1]
        army=h[2]
        pets=h[3]
        food=h[4]
        logs=h[5]
        metals=h[6]
        balance = discord.Embed(title='Player Balance',description='Amount of items in your cart')
        balance.add_field(name='Resources',value="{} coins\n{} cash\n{} food\n{} logs\n{} metals".format(coins,cash,food,logs,metals),inline=False)   
        balance.add_field(name='Animals',value="**Pets**\n{} Pets\n**Army**\n{} army animals".format(pets,army),inline=False)
        balance.add_field(name='Kingdom',value="Building 1\nBuilding 2\nBuilding 3\nBuilding 4\nBuilding 5\n",inline=False)
        await ctx.send(embed = balance)

def setup(client):
    client.add_cog(Finder(client))
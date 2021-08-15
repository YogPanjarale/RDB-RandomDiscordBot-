from logging import exception
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

    @commands.command(aliases=['nuser','make'],help ='create an account for this game') 
    @commands.cooldown(1,10,commands.BucketType.guild)
    async def newuser(self, ctx):
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
        animals = ['bear','Gator','narwhal','dragon','panthera','wolf']
        animalask=['army unit','pet']
        if place =='forest':
            number=25
            resource='logs'
            aa = r.randint(1,number)
            await ctx.send(f'you just got {aa} {resource} while exploring {place}')
            add(f'{ctx.author.id}',resource,aa,2)
        elif place =='caves':
            #aa=explore(2,'metal(s)','caves')
            number=2
            resource='metals'
            aa = r.randint(1,number)
            await ctx.send(f'you just got {aa} {resource} while exploring {place}')
            add(f'{ctx.author.id}',resource,aa,5)
        elif place =='savannah':
            #abc = explore(1,'animal(s)','savannah')
            abc= r.choice(animals)
            number=2
            aa = r.randint(1,number)
            aaa =r.choice(animalask)
            await ctx.send(f'you just found {aa} {abc} while exploring {place}')
            if aaa=='pet':
                resource='pets'
                add(f'{ctx.author.id}',resource,aa,5)
                await ctx.send(f"{abc} has been added as a pet")
            else:
                resource='army'
                add(f'{ctx.author.id}',resource,aa,2)
                await ctx.send(f"{abc} has been added as an army unit")
        elif place=='tunnels':
            #aa = explore(10,'coins','tunnels')
            number=10
            resource='coins'
            aa = r.randint(1,number)
            await ctx.send(f'you just got {aa} {resource} while exploring {place}')
            add(f'{ctx.author.id}',resource,aa,5)
        elif place=='plantations':
            #aa = explore(2,'fruit(s)','plantations')
            number=2
            resource='food'
            aa = r.randint(1,number)
            await ctx.send(f'you just got {aa} {resource} while exploring {place}')
            add(f'{ctx.author.id}',resource,aa,5)
        elif place=='loot':
            a=r.randint(1,10)
            if a==1:
                resource='cash'
                await ctx.send("Your luck seems nice , u just got some cash while exploring a random loot box and old taverns")
                add(f'{ctx.author.id}',resource,a,20)
            else:
                await ctx.send("sorry , this loot box seems to be empty , better luck next time")
        #else:
            #await ctx.send("sorry , you're not a registered member")

    @commands.command(aliases=['balance','items'],help ='check your balance and items that you have') 
    @commands.cooldown(1,10,commands.BucketType.guild)
    async def bal(self, ctx,member: Member = None):
        cur = m.connect(host='localhost',database='mgsb',user='MG',password='mg@123')
        game = cur.cursor()
        users = '''select coins,cash,army,pets,food,logs,metals,xp from player where name ="%s"'''
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
        XP = h[7]
        balance = discord.Embed(title='Player Balance',description=f'Amount of items in your cart\nPlayer XP = {XP}')
        balance.add_field(name='Resources',value="{} coins\n{} cash\n{} food\n{} logs\n{} metals".format(coins,cash,food,logs,metals),inline=False)   
        balance.add_field(name='Animals',value="**Pets**\n{} Pets\n**Army**\n{} army animals".format(pets,army),inline=False)
        balance.add_field(name='Kingdom',value="Building 1\nBuilding 2\nBuilding 3\nBuilding 4\nBuilding 5\n",inline=False)
        await ctx.send(embed = balance)
    @commands.command(aliases=['pets'],help ='explore the map to find items') 
    @commands.cooldown(1,10,commands.BucketType.user)
    async def pet(self, ctx,member: Member = None):
        cur = m.connect(host='localhost',database='mgsb',user='MG',password='mg@123')
        game = cur.cursor()
        users = '''select * from pets where name="%s"'''
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
        w1 = h[1]
        w1l=h[2]
        w2=h[3]
        w2l=h[4]
        p1=h[5]
        p1l=h[6]
        p2=h[7]
        p2l=h[8]
        d1=h[9]
        d1l=h[10]
        d2=h[11]
        d2l=h[12]
        b1=h[13]
        b1l=h[14]
        b2=h[15]
        b2l=h[16]
        s1=h[17]
        s1l=h[18]
        s2=h[19]
        s2l=h[20]
        e1=h[21]
        e1l=h[22]
        e2=h[23]
        e2l=h[24]
        Pets = discord.Embed(title='Pets',description=f'Pet names and Pets',color=discord.Colour.green())
        Pets.add_field(name=':wolf: Wolves :wolf:',value="Wolf 1's name = {} :wolf: \nlevel = {}%\nWolf 2's name = {} :wolf: \nlevel = {}%".format(w1,w1l,w2,w2l),inline=False)   
        Pets.add_field(name=':cat2: Pantheras :cat2:',value="Panthera 1's name = {} :tiger2: \nlevel = {}%\nPanthera 2's name = {} :tiger2: \nlevel = {}%".format(p1,p1l,p2,p2l),inline=False)
        Pets.add_field(name=':dragon: Dragons :dragon:',value="Dragon 1's name = {} :dragon: \nlevel = {}%\nDragon 2's name = {} :dragon: \nlevel = {}%".format(d1,d1l,d2,d2l),inline=False)
        Pets.add_field(name=':bear: Bears :bear:',value="Bear 1's name = {} :bear: \nlevel = {}%\nBear 2's name = {} :bear: \nlevel = {}%".format(b1,b1l,b2,b2l),inline=False)   
        Pets.add_field(name=':whale: Narwhals :whale:',value="Narwhal 1's name = {} :whale: \nlevel = {}%\nNarwhal 2's name = {} :whale: \nlevel = {}%".format(s1,s1l,s2,s2l),inline=False)
        Pets.add_field(name=':crocodile: Gator :crocodile:',value="Gator 1's name = {} :crocodile: \nlevel = {}%\nGator 2's name = {} :crocodile: \nlevel = {}%".format(e1,e1l,e2,e2l),inline=False)
        await ctx.send(embed = Pets)

def setup(client):
    client.add_cog(Finder(client))

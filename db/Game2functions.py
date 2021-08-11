import random as r
import mysql.connector as m
#create table new user function
def create(name):
    cur = m.connect(host='localhost',database='mgsb',user='MG',password='mg@123')
    game = cur.cursor()
    new =f'''insert into player(name,coins,cash,army,pets,food,logs,metals) values("{name}",0,0,0,0,0,0,0)
        ;'''
    game.execute(new)
    cur.commit()
    game.close()
#add values accordingly in the player table 
def add(name,coins,cash,army,pets,food,logs,metals):
    cur = m.connect(host='localhost',database='mgsb',user='MG',password='mg@123')
    game = cur.cursor()        
    a = '''update player
    set 
    coins=coins+%s,
    cash=cash+%s,
    army=army+%s,
    pets=pets+%s,
    food=food+%s,
    logs=logs+%s,
    metals=metals+%s
    where 
    name ="%s";
    '''
    params=(coins,cash,army,pets,food,logs,metals,name)
    b = a%params
    game.execute(b)
    cur.commit()
    game.close()

#print statement fucntion

#functions for getting all user data
def userdata(name):
    cur = m.connect(host='localhost',database='mgsb',user='MG',password='mg@123')
    game = cur.cursor()
    users = '''select * from player where name ="%s"'''
    s = name
    game.execute(users%s)
    l = game.fetchone()
    b = str(l).replace("[","")
    c=str(b).replace(']','')
    d = str(c).replace(',','')
    e=str(d).replace("'","")
    f=str(e).replace('(',"")
    g = str(f).replace(')','')

    game.close()
import random as r
import mysql.connector as m
#create table new user function

def create(name):
    cur = m.connect(host='localhost',database='mgsb',user='MG',password='mg@123')
    game = cur.cursor()
    new =f'''insert into player(name,coins,cash,army,pets,food,logs,metals,xp) values("{name}",0,0,0,0,0,0,0,0)
        ;'''
    new2 =f'''insert into pets(name,w1,w1l,w2,w2l,p1,p1l,p2,p2l,d1,d1l,d2,d2l,b1,b1l,b2,b2l,s1,s1l,s2,s2l,e1,e1l,e2,e2l) values("{name}",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        ;'''   
    game.execute(new)
    game.execute(new2)
    cur.commit()
    game.close()
#add values accordingly in the player table 
def add(name,resource,newnum,xp):
    cur = m.connect(host='localhost',database='mgsb',user='MG',password='mg@123')
    game = cur.cursor()        
    a = '''update player
    set 
    %s=%s+%s,
    xp=xp+%s
    where 
    name="%s";
    '''
    params=(resource,resource,newnum,xp,name)
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
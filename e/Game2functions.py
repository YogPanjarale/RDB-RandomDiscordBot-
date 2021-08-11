import random as r
import mysql.connector as m
cur = m.connect(host='localhost',database='mgsb',user='MG',password='mg@123')
game = cur.cursor()
#create table new user function
def create(name):
    cur = m.connect(host='localhost',database='mgsb',user='MG',password='mg@123')
    game = cur.cursor()
    new =f'''insert into players(name,coins,cash,army,pets,food,logs,metals) values("{name}",0,0,0,0,0,0,0)
        ;'''
    game.execute(new)
    cur.commit()
#add values accordingly in the player table 
def add(name,coins,cash,army,pets,food,logs,metals):
    cur = m.connect(host='localhost',database='mgsb',user='MG',password='mg@123')
    game = cur.cursor()
    try:           
        a = '''update players
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
        game.execute(a%params)
        cur.commit()
        game.close()
    except Exception as e:
        print(e)
#print statement fucntion
def explore(number,resource,inputs):
    aa = r.randint(1,number)
    print('you just got',aa,resource,'while exploring',inputs)
    return aa
#functions for getting all user data
def userdata(name):
    cur = m.connect(host='localhost',database='mgsb',user='MG',password='mg@123')
    game = cur.cursor()
    users = '''select coins,cash,army,pets,food,logs,metals from players where name ="%s"'''
    s = name
    game.execute(users%s)
    l = game.fetchall()
    b = str(l).replace("[","")
    c=str(b).replace(']','')
    d = str(c).replace(',','')
    e=str(d).replace("'","")
    f=str(e).replace('(',"")
    g = str(f).replace(')','')
    h=g.split(" ")
    coins = h[0]
    cash=h[1]
    army=h[2]
    pets=h[3]
    food=h[4]
    logs=h[5]
    metals=h[6]
    print("you have \n{} coins\n{} cash\n{}army units\n{} pets\n{} food\n{} logs\n{} metals".format(coins,cash,army,pets,food,logs,metals))
    game.close()
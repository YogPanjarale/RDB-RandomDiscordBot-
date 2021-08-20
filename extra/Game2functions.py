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
def pets(name):
    cur = m.connect(host='localhost',database='mgsb',user='MG',password='mg@123')
    game = cur.cursor()
    users = '''select * from pets where name="%s"'''
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
    print("Wolf 1's name = {} :wolf: \nlevel = {}%\nWolf 2's name = {} :wolf: \nlevel = {}%".format(w1,w1l,w2,w2l))
    print("Panthera 1's name = {} :tiger2: \nlevel = {}%\nPanthera 2's name = {} :tiger2: \nlevel = {}%".format(p1,p1l,p2,p2l))
    print("Dragon 1's name = {} :dragon: \nlevel = {}%\nDragon 2's name = {} :dragon: \nlevel = {}%".format(d1,d1l,d2,d2l))
    print("Bear 1's name = {} :bear: \nlevel = {}%\nBear 2's name = {} :bear: \nlevel = {}%".format(b1,b1l,b2,b2l))
    print("Narwhal 1's name = {} :whale: \nlevel = {}%\nNarwhal 2's name = {} :whale: \nlevel = {}%".format(s1,s1l,s2,s2l))
    print("Gator 1's name = {} :crocodile: \nlevel = {}%\nGator 2's name = {} :crocodile: \nlevel = {}%".format(e1,e1l,e2,e2l))
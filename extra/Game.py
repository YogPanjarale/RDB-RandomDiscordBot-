import mysql.connector as m
import random as r
from datetime import *
from time import sleep
import sys
from Game2functions import *
#cursor
cur = m.connect(host='localhost',database='mgsb',user='MG',password='mg@123')
game = cur.cursor()
#player tables 
tables = '''select name from players;'''
game.execute(tables)
l = game.fetchall()
a = list(l)
b = str(a).replace("[","")
c=str(b).replace(']','')
d = str(c).replace(',','')
e=str(d).replace("'","")
f=str(e).replace('(',"")
g = str(f).replace(')','')
print('Current player accounts :-\n'+g)
#login
playername=input("enter your name please:\n")
#resources list
Explore = ['wood','metal','coins','animals','fruit','cash']
#explore items dictionary
explore_range = {'wood':25,'metal':2,'coins':10,'fruit':2,'cash':1,'animals':1,'rocks':2}
#starting input
if playername not in g:
    agreed = input("You seem like a new player , should we create a record for u: (say 'y' for yes and 'n' for no)\n")
    if agreed=='y':
        create(playername)
        print("player has been created , restart game please")
        sys.exit()
    else:
        print("k , whatever")
        sys.exit()

else:
    while True:
        wtd = input("what would you like to do:\n")
        animals = ['dog','fox','bear','pig','frog','monkey','narwhal','dodo','eagle','shark','bull','dragon']
        if wtd=='e':
            explores = input("where would u like to go exploring:\n")
            if explores =='forest':
                aa=explore(25,'log(s)','forest')
                add(f'{playername}',0,0,0,0,0,aa,0)
            elif explores =='caves':
                aa=explore(2,'metal(s)','caves')
                add(f'{playername}',0,0,0,0,0,0,aa)
            elif explores =='savannah':
                abc = explore(1,'animal(s)','savannah')
                abc= r.choice(animals)
                animalask = input(f"you found a(n) {abc} , would you like to keep it as a pet or as an army unit? (use 'pet' for pet and 'au' for army unit:\n")
                if animalask=='pet':
                    add(f'{playername}',0,0,0,1,0,0,0)
                    print("animal has been added as a pet")
                else:
                    add(f'{playername}',0,0,1,0,0,0,0)
                    print("animal has been added as an army unit")
            elif explores=='tunnels':
                aa = explore(10,'coins','tunnels')
                add(f'{playername}',aa,0,0,0,0,0,0)
            elif explores=='plantations':
                aa = explore(2,'fruit(s)','plantations')
                add(f'{playername}',0,0,0,0,aa,0,0)
            elif explores=='loot':
                a=r.randint(1,10)
                if a==1:
                    print("wow , your luck seems nice , u just got some cash while exploring a random loot box and old taverns")
                    add(f'{playername}',0,2,0,0,0,0,0)
                else:
                    print("sorry , this loot box seems to be empty , better luck next time")
            continue
        elif wtd=='bal':
            userdata(playername)
            continue

        
        






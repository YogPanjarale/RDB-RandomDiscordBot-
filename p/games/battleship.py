import random
import sys
print("We are playing Battleship!!!")
print("Rules of the game are very simple. There will be a 5X5 grid, in which 3 battleships will be placed on random positions and you have to destroy them. You have to guess the postion of battleships and if you get them right in 20 chances then you win and you have 2 hints.")
print()
B1=''
B2=''
B3=''
B=[B1,B2,B3]
BCount=0

def hint(c):
    k=random.choice(B)
    k1=k[0]
    c1=c[0]
    x=alpha.index(k1)-alpha.index(c1)
    y=int(k[1])-int(c[1])
    if x<0:
        x*=-1
    if y<0:
        y*=-1
    r=random.choice([x+1,y+1])
    return r

alpha=['a','b','c','d','e','f']

ch=20

a1='   '
a2='   '
a3='   '
a4='   '
a5='   '
b1='   '
b2='   '
b3='   '
b4='   '
b5='   '
c1='   '
c2='   '
c3='   '
c4='   '
c5='   '
d1='   '
d2='   '
d3='   '
d4='   '
d5='   '
e1='   '
e2='   '
e3='   '
e4='   '
e5='   '
f1='   '
f2='   '
f3='   '
f4='   '
f5='   '
l=[[a1,a2,a3,a4,a5],[b1,b2,b3,b4,b5],[c1,c2,c3,c4,c5],[d1,d2,d3,d4,d5],[e1,e2,e3,e4,e5],[f1,f2,f3,f4,f5]]
l1=[['a1','a2','a3','a4','a5'],['b1','b2','b3','b4','b5'],['c1','c2','c3','c4','c5'],['d1','d2','d3','d4','d5'],['e1','e2','e3','e4','e5'],['f1','f2','f3','f4','f5']]
l2=['a1','a2','a3','a4','a5','b1','b2','b3','b4','b5','c1','c2','c3','c4','c5','d1','d2','d3','d4','d5','e1','e2','e3','e4','e5','f1','f2','f3','f4','f5']

for k in range(3):
    while True:
        r=random.choice(l2)
        if r not in B:
            break
    B[k]=r

c=1
h=0
if c!=1:
    print("If you want hint then write 'hint' instead of the position!")
while c<=ch:
    c+=1
    while True:
        i=input("Enter position:")
        print()
        i=i.lower()
        
        if i=='hint':
            if c!=2:
                if h<2:
                    h+=1
                    print("Hint:",hint(i0),'is the difference between their x or y coordinates')
                else:
                    print("You can't take anymore hints!")
            else:
                print("You can't take hint in the first chance!")
        else:
            if len(i)!=2:
                print("Invalid Input!")
            else:
                if i[0] not in 'abcdef' or i[1] not in '12345':
                    print("Invalid Input!")
                else:
                    if i not in l2:
                        print("Invaild Input!")
                    else:
                        l2.remove(i)
                        i0=i

                        if i not in B:
                            for j in range(6):
                                for k in range(5):
                                    if l1[j][k]==i:
                                        l[j][k]=' X '

                        
                        if i not in B:
                            print("      1       2       3       4       5    ")
                            print("  +-------+-------+-------+-------+-------+")
                            print("a | ",l[0][0]," | ",l[0][1]," | ",l[0][2]," | ",l[0][3]," | ",l[0][4]," |")
                            print("  +-------+-------+-------+-------+-------+")
                            print("b | ",l[1][0]," | ",l[1][1]," | ",l[1][2]," | ",l[1][3]," | ",l[1][4]," |")
                            print("  +-------+-------+-------+-------+-------+")
                            print("c | ",l[2][0]," | ",l[2][1]," | ",l[2][2]," | ",l[2][3]," | ",l[2][4]," |")
                            print("  +-------+-------+-------+-------+-------+")
                            print("d | ",l[3][0]," | ",l[3][1]," | ",l[3][2]," | ",l[3][3]," | ",l[3][4]," |")
                            print("  +-------+-------+-------+-------+-------+")
                            print("e | ",l[4][0]," | ",l[4][1]," | ",l[4][2]," | ",l[4][3]," | ",l[4][4]," |")
                            print("  +-------+-------+-------+-------+-------+")
                            print("f | ",l[5][0]," | ",l[5][1]," | ",l[5][2]," | ",l[5][3]," | ",l[5][4]," |")
                            print("  +-------+-------+-------+-------+-------+")
                        break
    
    if i in B:

        for j in range(6):
            for k in range(5):
                if l1[j][k]==i:
                    if BCount==0:
                        l[j][k]=' B1'
                    elif BCount==1:
                        l[j][k]=' B2'
                    else:
                        l[j][k]=' B3'


        print()
        print("      1       2       3       4       5    ")
        print("  +-------+-------+-------+-------+-------+")
        print("a | ",l[0][0]," | ",l[0][1]," | ",l[0][2]," | ",l[0][3]," | ",l[0][4]," |")
        print("  +-------+-------+-------+-------+-------+")
        print("b | ",l[1][0]," | ",l[1][1]," | ",l[1][2]," | ",l[1][3]," | ",l[1][4]," |")
        print("  +-------+-------+-------+-------+-------+")
        print("c | ",l[2][0]," | ",l[2][1]," | ",l[2][2]," | ",l[2][3]," | ",l[2][4]," |")
        print("  +-------+-------+-------+-------+-------+")
        print("d | ",l[3][0]," | ",l[3][1]," | ",l[3][2]," | ",l[3][3]," | ",l[3][4]," |")
        print("  +-------+-------+-------+-------+-------+")
        print("e | ",l[4][0]," | ",l[4][1]," | ",l[4][2]," | ",l[4][3]," | ",l[4][4]," |")
        print("  +-------+-------+-------+-------+-------+")
        print("f | ",l[5][0]," | ",l[5][1]," | ",l[5][2]," | ",l[5][3]," | ",l[5][4]," |")
        print("  +-------+-------+-------+-------+-------+")
        print()

        print("You destroyed a battleship!!")
        B.remove(i)
        BCount+=1

    if B==[]:
        print()
        print("YOU DESTROYED ALL THE BATTLESHIPS!!!")
        print("YOU WON!!!")
        break
    else:
        if c==ch+1:
            print("YOU LOSE!!!")
            print("Battleship/s was/were at",end=' ')
            for i in B:
                if i!=B[-1]:
                    print(i,end=',')
                else:
                    print(i,end='.')
            break

    print()
    print("You have -",ch-c+1,'chances left')
    
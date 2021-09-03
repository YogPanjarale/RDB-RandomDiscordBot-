import random

a1=' '
a2=' '
a3=' '
a4=' '
a5=' '
a6=' '
b1=' '
b2=' '
b3=' '
b4=' '
b5=' '
b6=' '
c1=' '
c2=' '
c3=' '
c4=' '
c5=' '
c6=' '
d1=' '
d2=' '
d3=' '
d4=' '
d5=' '
d6=' '
e1=' '
e2=' '
e3=' '
e4=' '
e5=' '
e6=' '
f1=' '
f2=' '
f3=' '
f4=' '
f5=' '
f6=' '

l=[[a1,a2,a3,a4,a5,a6],[b1,b2,b3,b4,b5,b6],[c1,c2,c3,c4,c5,c6],[d1,d2,d3,d4,d5,d6],[e1,e2,e3,e4,e5,e6],[f1,f2,f3,f4,f5,f6]]
l1=[['a1','a2','a3','a4','a5','a6'],['b1','b2','b3','b4','b5','b6'],['c1','c2','c3','c4','c5','c6'],['d1','d2','d3','d4','d5','d6'],['e1','e2','e3','e4','e5','e6'],['f1','f2','f3','f4','f5','f6']]
l2=['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6','c1','c2','c3','c4','c5','c6','d1','d2','d3','d4','d5','d6','e1','e2','e3','e4','e5','e6','f1','f2','f3','f4','f5','f6']
lp=[]
lc=[]
li=[]

def grid():
    print()
    print("+-----+-----+-----+-----+-----+-----+")
    print("| ",l[0][0]," | ",l[0][1]," | ",l[0][2]," | ",l[0][3]," | ",l[0][4]," | ",l[0][5]," |")
    print("+-----+-----+-----+-----+-----+-----+")
    print("| ",l[1][0]," | ",l[1][1]," | ",l[1][2]," | ",l[1][3]," | ",l[1][4]," | ",l[1][5]," |")
    print("+-----+-----+-----+-----+-----+-----+")
    print("| ",l[2][0]," | ",l[2][1]," | ",l[2][2]," | ",l[2][3]," | ",l[2][4]," | ",l[2][5]," |")
    print("+-----+-----+-----+-----+-----+-----+")
    print("| ",l[3][0]," | ",l[3][1]," | ",l[3][2]," | ",l[3][3]," | ",l[3][4]," | ",l[3][5]," |")
    print("+-----+-----+-----+-----+-----+-----+")
    print("| ",l[4][0]," | ",l[4][1]," | ",l[4][2]," | ",l[4][3]," | ",l[4][4]," | ",l[4][5]," |")
    print("+-----+-----+-----+-----+-----+-----+")
    print("| ",l[5][0]," | ",l[5][1]," | ",l[5][2]," | ",l[5][3]," | ",l[5][4]," | ",l[5][5]," |")
    print("+-----+-----+-----+-----+-----+-----+")
    print()

print("Let's play Obstruction!!!")

while True:
    p=input("Choose X or O >")
    p=p.upper()
    if p=='X':
        c='O'
        break
    elif p=='O':
        c='X'
        break
    else:
        print("Invalid Input!")
        continue

if p=='X':
    print("You will start!")
    while True:
        print("YOUR TURN")
        if len(l2)==0:
            print("I WIN!!!")
            break
        while True:
            while True:
                x=input("Where do you want to put X?")
                #print(lp)
                if x in l2:
                    if x in lp or x in lc:
                        print("Illegal Input!")
                        li.append(x)
                        continue
                    else:
                        break
                else:
                    print("Invalid Input!")
                    continue
            l2.remove(x)
            
            for i in range(6):
                for j in range(6):
                    if l1[i][j]==x:
                        l[i][j]='X'
                        if x in ['a1','a2','a3','a4','a5','a6','f1','f2','f3','f4','f5','f6','b1','c1','d1','e1','b6','c6','d6','e6']:
                            if x in ['a2','a3','a4','a5']:
                                lp.append(l1[i][j])
                                lp.append(l1[i][j+1])
                                lp.append(l1[i][j-1])
                                lp.append(l1[i+1][j])
                                lp.append(l1[i+1][j+1])
                                lp.append(l1[i+1][j-1])
                            elif x in ['f2','f3','f4','f5']:
                                lp.append(l1[i][j])
                                lp.append(l1[i][j+1])
                                lp.append(l1[i][j-1])
                                lp.append(l1[i-1][j])
                                lp.append(l1[i-1][j+1])
                                lp.append(l1[i-1][j-1])
                            elif x in ['b1','c1','d1','e1']:
                                lp.append(l1[i][j])
                                lp.append(l1[i+1][j])
                                lp.append(l1[i-1][j])
                                lp.append(l1[i][j+1])
                                lp.append(l1[i+1][j+1])
                                lp.append(l1[i-1][j+1])
                            elif x in ['b6','c6','d6','e6']:
                                lp.append(l1[i][j])
                                lp.append(l1[i+1][j])
                                lp.append(l1[i-1][j])
                                lp.append(l1[i][j-1])
                                lp.append(l1[i+1][j-1])
                                lp.append(l1[i-1][j-1])
                            elif x=='a1':
                                lp.append('a2')
                                lp.append('b1')
                                lp.append('b2')
                            elif x=='f1':
                                lp.append('e1')
                                lp.append('e2')
                                lp.append('f2')
                            elif x=='a6':
                                lp.append('a5')
                                lp.append('b6')
                                lp.append('b5')
                            elif x=='f6':
                                lp.append('f5')
                                lp.append('e5')
                                lp.append('e6')
                        else:
                            lp.append(l1[i][j])
                            lp.append(l1[i][j+1])
                            lp.append(l1[i][j-1])
                            lp.append(l1[i+1][j])
                            lp.append(l1[i+1][j+1])
                            lp.append(l1[i+1][j-1])
                            lp.append(l1[i-1][j])
                            lp.append(l1[i-1][j+1])
                            lp.append(l1[i-1][j-1])
            break                                    
        
        grid()
        
        print("MY TURN")
        print(li)
        print(l2)
        if li==l2:
            print("YOU WIN!!!")
            break
        while True:
            while True:
                y=random.choice(l2)
                if y in lp or y in lc:
                    li.append(y)
                    continue
                else:
                    break
            l2.remove(y)
            print("I have put O at",y)
            for i in range(6):
                for j in range(6):
                    if l1[i][j]==y:
                        l[i][j]='O'
                        if y in ['a1','a2','a3','a4','a5','a6','f1','f2','f3','f4','f5','f6','b1','c1','d1','e1','b6','c6','d6','e6']:
                            if y in ['a2','a3','a4','a5']:
                                lc.append(l1[i][j])
                                lc.append(l1[i][j+1])
                                lc.append(l1[i][j-1])
                                lc.append(l1[i+1][j])
                                lc.append(l1[i+1][j+1])
                                lc.append(l1[i+1][j-1])
                            elif y in ['f2','f3','f4','f5']:
                                lc.append(l1[i][j])
                                lc.append(l1[i][j+1])
                                lc.append(l1[i][j-1])
                                lc.append(l1[i-1][j])
                                lc.append(l1[i-1][j+1])
                                lc.append(l1[i-1][j-1])
                            elif y in ['b2','c2','d2','e2']:
                                lc.append(l1[i][j])
                                lc.append(l1[i+1][j])
                                lc.append(l1[i-1][j])
                                lc.append(l1[i][j+1])
                                lc.append(l1[i+1][j+1])
                                lc.append(l1[i-1][j+1])
                            elif y in ['b6','c6','d6','e6']:
                                lc.append(l1[i][j])
                                lc.append(l1[i+1][j])
                                lc.append(l1[i-1][j])
                                lc.append(l1[i][j-1])
                                lc.append(l1[i+1][j-1])
                                lc.append(l1[i-1][j-1])
                            elif y=='a1':
                                lc.append('a2')
                                lc.append('b1')
                                lc.append('b2')
                            elif y=='f1':
                                lc.append('e1')
                                lc.append('e2')
                                lc.append('f2')
                            elif y=='a6':
                                lc.append('a5')
                                lc.append('b6')
                                lc.append('b5')
                            elif y=='f6':
                                lc.append('f5')
                                lc.append('e5')
                                lc.append('e6')
                        else:
                            lc.append(l1[i][j])
                            lc.append(l1[i][j+1])
                            lc.append(l1[i][j-1])
                            lc.append(l1[i+1][j])
                            lc.append(l1[i+1][j+1])
                            lc.append(l1[i+1][j-1])
                            lc.append(l1[i-1][j])
                            lc.append(l1[i-1][j+1])
                            lc.append(l1[i-1][j-1])
            break
    
        grid()

elif p=='O':
    print("I will start!")
    while True:
        print("MY TURN")
        if li==l2:
            print("YOU WIN!!!")
            break
        while True:
            while True:
                y=random.choice(l2)
                if y in lp or y in lc:
                    continue
                else:
                    break
            l2.remove(y)
            print("I have put X at",y)
            for i in range(6):
                for j in range(6):
                    if l1[i][j]==y:
                        l[i][j]='X'
                        if y in ['a1','a2','a3','a4','a5','a6','f1','f2','f3','f4','f5','f6','b1','c1','d1','e1','b6','c6','d6','e6']:
                            if y in ['a2','a3','a4','a5']:
                                lc.append(l1[i][j])
                                lc.append(l1[i][j+1])
                                lc.append(l1[i][j-1])
                                lc.append(l1[i+1][j])
                                lc.append(l1[i+1][j+1])
                                lc.append(l1[i+1][j-1])
                            elif y in ['f2','f3','f4','f5']:
                                lc.append(l1[i][j])
                                lc.append(l1[i][j+1])
                                lc.append(l1[i][j-1])
                                lc.append(l1[i-1][j])
                                lc.append(l1[i-1][j+1])
                                lc.append(l1[i-1][j-1])
                            elif y in ['b2','c2','d2','e2']:
                                lc.append(l1[i][j])
                                lc.append(l1[i+1][j])
                                lc.append(l1[i-1][j])
                                lc.append(l1[i][j+1])
                                lc.append(l1[i+1][j+1])
                                lc.append(l1[i-1][j+1])
                            elif y in ['b6','c6','d6','e6']:
                                lp.append(l1[i][j])
                                lp.append(l1[i+1][j])
                                lp.append(l1[i-1][j])
                                lp.append(l1[i][j-1])
                                lp.append(l1[i+1][j-1])
                                lp.append(l1[i-1][j-1])
                            elif y=='a1':
                                lc.append('a2')
                                lc.append('b1')
                                lc.append('b2')
                            elif y=='f1':
                                lc.append('e1')
                                lc.append('e2')
                                lc.append('f2')
                            elif y=='a6':
                                lc.append('a5')
                                lc.append('b6')
                                lc.append('b5')
                            elif y=='f6':
                                lc.append('f5')
                                lc.append('e5')
                                lc.append('e6')
                        else:
                            lc.append(l1[i][j])
                            lc.append(l1[i][j+1])
                            lc.append(l1[i][j-1])
                            lc.append(l1[i+1][j])
                            lc.append(l1[i+1][j+1])
                            lc.append(l1[i+1][j-1])
                            lc.append(l1[i-1][j])
                            lc.append(l1[i-1][j+1])
                            lc.append(l1[i-1][j-1])
            break
    
        grid()

        print("YOUR TURN")
        if li==l2:
            print("I WIN!!!")
            break
        while True:
            while True:
                x=input("Where do you want to put O?")
                if x in l2:
                    if x in lp or x in lc:
                        print("Illegal Input!")
                        continue
                    else:
                        break
                else:
                    print("Invalid Input!")
                    continue
            l2.remove(x)
            
            for i in range(6):
                for j in range(6):
                    if l1[i][j]==x:
                        l[i][j]='O'
                        i-=1
                        j-=1
                        if x in ['a1','a2','a3','a4','a5','a6','f1','f2','f3','f4','f5','f6','b1','c1','d1','e1','b6','c6','d6','e6']:
                            if x in ['a2','a3','a4','a5']:
                                lp.append(l1[i][j])
                                lp.append(l1[i][j+1])
                                lp.append(l1[i][j-1])
                                lp.append(l1[i+1][j])
                                lp.append(l1[i+1][j+1])
                                lp.append(l1[i+1][j-1])
                            elif x in ['f2','f3','f4','f5']:
                                lp.append(l1[i][j])
                                lp.append(l1[i][j+1])
                                lp.append(l1[i][j-1])
                                lp.append(l1[i-1][j])
                                lp.append(l1[i-1][j+1])
                                lp.append(l1[i-1][j-1])
                            elif x in ['b1','c1','d1','e1']:
                                lp.append(l1[i][j])
                                lp.append(l1[i+1][j])
                                lp.append(l1[i-1][j])
                                lp.append(l1[i][j+1])
                                lp.append(l1[i+1][j+1])
                                lp.append(l1[i-1][j+1])
                            elif x in ['b6','c6','d6','e6']:
                                lp.append(l1[i][j])
                                lp.append(l1[i][j+1])
                                lp.append(l1[i][j-1])
                                lp.append(l1[i-1][j])
                                lp.append(l1[i-1][j+1])
                                lp.append(l1[i-1][j-1])
                            elif x=='a1':
                                lp.append('a2')
                                lp.append('b1')
                                lp.append('b2')
                            elif x=='f1':
                                lp.append('e1')
                                lp.append('e2')
                                lp.append('f2')
                            elif x=='a6':
                                lp.append('a5')
                                lp.append('b6')
                                lp.append('b5')
                            elif x=='f6':
                                lp.append('f5')
                                lp.append('e5')
                                lp.append('e6')
                        else:
                            lp.append(l1[i][j])
                            lp.append(l1[i][j+1])
                            lp.append(l1[i][j-1])
                            lp.append(l1[i+1][j])
                            lp.append(l1[i+1][j+1])
                            lp.append(l1[i+1][j-1])
                            lp.append(l1[i-1][j])
                            lp.append(l1[i-1][j+1])
                            lp.append(l1[i-1][j-1])
            break                                    
        
        grid()
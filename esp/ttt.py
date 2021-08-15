import random

print("Let's play Tic-Tac-Toe!!!")

tl=''
tm=''
tr=''
ml=''
mm=''
mr=''
bl=''
bm=''
br=''

l=[[tl,tm,tr],[ml,mm,mr],[bl,bm,br]]
l1=[['tl','tm','tr'],['ml','mm','mr'],['bl','bm','br']]
l2=['tl','tm','tr','ml','mm','mr','bl','bm','br']

def check_1(list):
    for i in range(3):
        if list[i][0]==list[i][1] and list[i][0]==list[i][2] and list[i][0]!='':
            return list[i][0]
        elif list[0][i]==list[1][i] and list[0][i]==list[2][i] and list[0][i]!='':  
            return list[0][i]
        elif list[0][0]==list[1][1] and list[0][0]==list[2][2] and list[0][0]!='':
            return list[0][0] 
        elif list[0][2]==list[1][1] and list[0][2]==list[2][0] and list[0][2]!='':
            return list[0][2]
    else:
        return ''

while True:
    n=input("How many players are playing?")
    if n=='1':
        while True:
            a=input("Choose: x or o >")
            p=a.lower()
            if p not in ('x','o'):
                print("Invalid input")
                continue
            else:
                break

        if p=='x':
            c='o'
            print("You have chosen x and therefore I have o")
        elif p=='o':
            c='x'
            print("You have chosen o and therefore I have x")
        print("Name of the cells are tl for top left, tm for top middle, tr for top right, ml for middle left, mm for middle middle, mr for middle right, bl for bottom left, bm for bottom middle, br for bottom right.")
        print("Best of luck!!")
        print("Let the battle begin!!")

        def check_2():
            for i in range(3):
                if l[i][0]==l[i][1] and l[i][2]=='' and l[i][0]!='':
                    return l1[i][2]
                elif l[i][0]==l[i][2] and l[i][1]=='' and l[i][0]!='':
                    return l1[i][1]
                elif l[i][1]==l[i][2] and l[i][0]=='' and l[i][1]!='':
                    return l1[i][0]
                elif l[0][i]==l[1][i] and l[2][i]=='' and l[0][i]!='':
                    return l1[2][i]
                elif l[0][i]==l[2][i] and l[1][i]=='' and l[0][i]!='':
                    return l1[1][i]
                elif l[1][i]==l[2][i] and l[0][i]=='' and l[1][i]!='':
                    return l1[0][i]
            else:
                if l[0][0]==l[1][1] and l[2][2]=='' and l[0][0]!='':
                    return l1[2][2]
                elif l[0][0]==l[2][2] and l[1][1]=='' and l[0][0]!='':
                    return l1[1][1]
                elif l[1][1]==l[2][2] and l[0][0]=='' and l[1][1]!='':
                    return l1[0][0]
                elif l[0][2]==l[1][1] and l[2][0]=='' and l[0][2]!='':
                    return l1[2][0]
                elif l[0][2]==l[2][0] and l[1][1]=='' and l[0][2]!='':
                    return l1[1][1]
                elif l[2][0]==l[1][1] and l[0][2]=='' and l[2][0]!='':
                    return l1[0][2]
                else:
                    return ''

        if c=='x':
            print("I will start!")
            r=random.choice(['t1'])
            print(r)
            if r=='t1':
                i=0
                l3=['tl','tr','bl','br']
                while True:
                    i+=1
                    
                    j=check_2()
                    if j=='':
                        if i==1:
                            x=random.choice(l3)
                            l3.remove(x)
                            l2.remove(x)
                        elif i!=1:
                            if 'mm' not in l2:
                                if l3!=[]:
                                    print(1)
                                    x=random.choice(l3)
                                    print(x)
                                    l3.remove(x)
                                    l2.remove(x)
                                else:
                                    print(2)
                                    x=random.choice(l2)
                                    print(x)
                                    l2.remove(x)

                            else:
                                x=random.choice(l2)
                                l2.remove(x)
                                if x in l3:
                                    l3.remove(x)

                    else:
                        x=j
                        l2.remove(x)
                        if x in l3:
                            l3.remove(x)

                    for i in range(3):
                        for j in range(3):
                            if l1[i][j]==x:
                                l[i][j]='x'

                    print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                    print("------------------")
                    print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                    print("------------------")
                    print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                    print()
                    print()


                    print(f"I have put x at {x}")

                    k=check_1(l)
                    if k=='o':
                        print("You won!!")
                        break
                    elif k=='x':
                        print("I won!!")
                        break
                    elif k=='':
                        if l2==[]:
                            print("Draw!!")
                            break

                    while True:
                        x1=str(input(f"Where do you want to put o?"))
                        if x1 not in l2:
                            print("Invalid input")
                            continue
                        else:
                            break
                    l2.remove(x1)
                    if x1 in l3:
                        l3.remove(x1)

                    for i in range(3):
                        for j in range(3):
                            if l1[i][j]==x1:
                                l[i][j]='o'     

                    print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                    print("------------")
                    print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                    print("------------")
                    print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                    print()
                    print()

                    k=check_1(l)
                    if k=='o':
                        print("You won!!")
                        break
                    elif k=='x':
                        print("I won!!")
                        break
                    elif k=='':
                        if l2==[]:
                            print("Draw!!")
                            break

            elif r=='t2':
                for i in range(3):
                    for j in range(3):
                        if l1[i][j]=='mm':
                            l[i][j]='x'
                            l2.remove('mm')

                print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                print("------------")
                print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                print("------------")
                print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                print()
                print()
                        
                while True:
                    x=str(input(f"Where do you want to put o?"))
                    if x not in l2:
                        print("Invalid input")
                        continue
                    else:
                        break

                for i in range(3):
                    for j in range(3):
                        if l1[i][j]==x:
                            l[i][j]='o'
                            l2.remove(x)
                
                print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                print("------------")
                print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                print("------------")
                print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                print()
                print()

                if x in ['tm','ml','mr','bm']:
                    if x=='tm':
                        y=random.choice(['tl','tr'])
                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==y:
                                    l[i][j]='x'
                                    l2.remove(y)
                        
                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                        while True:
                            x1=str(input(f"Where do you want to put o?"))
                            if x1 not in l2:
                                print("Invalid input")
                                continue
                            else:
                                break
                        l2.remove(x1)

                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==x1:
                                    l[i][j]='o'

                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                        k=check_1(l)
                        if k=='o':
                            print("You won!!")
                            break
                        elif k=='x':
                            print("I won!!")
                            break
                        elif k=='':
                            if l2==[]:
                                print("Draw!!")
                                break                             

                        if y=='tl':
                            for i in range(3):
                                for j in range(3):
                                    if l1[i][j]=='bl':
                                        l[i][j]='x'

                        elif y=='tr':
                            for i in range(3):
                                for j in range(3):
                                    if l1[i][j]=='br':
                                        l[i][j]='x'
                        
                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                        while True:
                            x1=str(input(f"Where do you want to put o?"))
                            if x1 not in l2:
                                print("Invalid input")
                                continue
                            else:
                                break
                        l2.remove(x1)

                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==x1:
                                    l[i][j]='o'

                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                        c=check_2()
                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==c:
                                    l[i][j]='x'
                        l2.remove(c)
                        
                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                        k=check_1(l)
                        if k=='o':
                            print("You won!!")
                            break
                        elif k=='x':
                            print("I won!!")
                            break
                        elif k=='':
                            if l2==[]:
                                print("Draw!!")
                                break

                        c=check_2()
                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==c:
                                    l[i][j]='x'
                        l2.remove(c)

                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                    elif x=='ml':
                        y=random.choice(['tl','bl'])
                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==y:
                                    l[i][j]='x'
                                    l2.remove(y)
                        
                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                        while True:
                            x1=str(input(f"Where do you want to put o?"))
                            if x1 not in l2:
                                print("Invalid input")
                                continue
                            else:
                                break
                        l2.remove(x1)

                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==x1:
                                    l[i][j]='o'

                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                        k=check_1(l)
                        if k=='o':
                            print("You won!!")
                            break
                        elif k=='x':
                            print("I won!!")
                            break
                        elif k=='':
                            if l2==[]:
                                print("Draw!!")
                                break                             

                        if y=='tl':
                            for i in range(3):
                                for j in range(3):
                                    if l1[i][j]=='tr':
                                        l[i][j]='x'

                        elif y=='bl':
                            for i in range(3):
                                for j in range(3):
                                    if l1[i][j]=='br':
                                        l[i][j]='x'
                        
                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                        while True:
                            x1=str(input(f"Where do you want to put o?"))
                            if x1 not in l2:
                                print("Invalid input")
                                continue
                            else:
                                break
                        l2.remove(x1)

                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==x1:
                                    l[i][j]='o'

                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                        c=check_2()
                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==c:
                                    l[i][j]='x'
                        l2.remove(c)
                        
                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                        k=check_1(l)
                        if k=='o':
                            print("You won!!")
                            break
                        elif k=='x':
                            print("I won!!")
                            break
                        elif k=='':
                            if l2==[]:
                                print("Draw!!")
                                break

                        c=check_2()
                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==c:
                                    l[i][j]='x'
                        l2.remove(c)

                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()
                    
                    elif x=='mr':
                        y=random.choice(['tr','br'])
                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==y:
                                    l[i][j]='x'
                                    l2.remove(y)
                        
                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                        while True:
                            x1=str(input(f"Where do you want to put o?"))
                            if x1 not in l2:
                                print("Invalid input")
                                continue
                            else:
                                break
                        l2.remove(x1)

                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==x1:
                                    l[i][j]='o'

                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                        k=check_1(l)
                        if k=='o':
                            print("You won!!")
                            break
                        elif k=='x':
                            print("I won!!")
                            break
                        elif k=='':
                            if l2==[]:
                                print("Draw!!")
                                break                             

                        if y=='tr':
                            for i in range(3):
                                for j in range(3):
                                    if l1[i][j]=='tl':
                                        l[i][j]='x'

                        elif y=='br':
                            for i in range(3):
                                for j in range(3):
                                    if l1[i][j]=='bl':
                                        l[i][j]='x'
                        
                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                        while True:
                            x1=str(input(f"Where do you want to put o?"))
                            if x1 not in l2:
                                print("Invalid input")
                                continue
                            else:
                                break
                        l2.remove(x1)

                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==x1:
                                    l[i][j]='o'

                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                        c=check_2()
                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==c:
                                    l[i][j]='x'
                        l2.remove(c)
                        
                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                        k=check_1(l)
                        if k=='o':
                            print("You won!!")
                            break
                        elif k=='x':
                            print("I won!!")
                            break
                        elif k=='':
                            if l2==[]:
                                print("Draw!!")
                                break

                        c=check_2()
                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==c:
                                    l[i][j]='x'
                        l2.remove(c)

                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                    elif x=='bm':
                        y=random.choice(['bl','br'])
                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==y:
                                    l[i][j]='x'
                                    l2.remove(y)
                        
                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                        while True:
                            x1=str(input(f"Where do you want to put o?"))
                            if x1 not in l2:
                                print("Invalid input")
                                continue
                            else:
                                break
                        l2.remove(x1)

                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==x1:
                                    l[i][j]='o'

                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                        k=check_1(l)
                        if k=='o':
                            print("You won!!")
                            break
                        elif k=='x':
                            print("I won!!")
                            break
                        elif k=='':
                            if l2==[]:
                                print("Draw!!")
                                break                             

                        if y=='bl':
                            for i in range(3):
                                for j in range(3):
                                    if l1[i][j]=='tl':
                                        l[i][j]='x'

                        elif y=='br':
                            for i in range(3):
                                for j in range(3):
                                    if l1[i][j]=='tr':
                                        l[i][j]='x'
                        
                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                        while True:
                            x1=str(input(f"Where do you want to put o?"))
                            if x1 not in l2:
                                print("Invalid input")
                                continue
                            else:
                                break
                        l2.remove(x1)

                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==x1:
                                    l[i][j]='o'

                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                        c=check_2()
                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==c:
                                    l[i][j]='x'
                        l2.remove(c)
                        
                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

                        k=check_1(l)
                        if k=='o':
                            print("You won!!")
                            break
                        elif k=='x':
                            print("I won!!")
                            break
                        elif k=='':
                            if l2==[]:
                                print("Draw!!")
                                break

                        c=check_2()
                        for i in range(3):
                            for j in range(3):
                                if l1[i][j]==c:
                                    l[i][j]='x'
                        l2.remove(c)

                        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                        print("------------")
                        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                        print("------------")
                        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                        print()
                        print()

        elif p=='x':
            print("You will start!")
            i=0
            l3=['tl','tr','bl','br']  
            while True:
                i+=1

                while True:
                    x1=str(input("Where do you want to put x?"))
                    if x1 not in l2:
                        print("Invalid input")
                        continue
                    else:
                        break
                l2.remove(x1)
                if x1 in l3:
                    l3.remove(x1)

                for i in range(3):
                    for j in range(3):
                        if l1[i][j]==x1:
                            l[i][j]='x'      

                print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                print("------------")
                print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                print("------------")
                print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                print()
                print()

                k=check_1(l)
                if k=='x':
                    print("You won!!")
                    break
                elif k=='o':
                    print("I won!!")
                    break
                elif k=='':
                    if l2==[]:
                        print("Draw!!")
                        break
                
                j=check_2()
                if j=='':
                    if i==1:
                        x=random.choice(l3)
                        l3.remove(x)
                        l2.remove(x)
                    elif i!=1:
                        if 'mm' not in l2:
                            if l3!=[]:
                                print(1)
                                x=random.choice(l3)
                                print(x)
                                l3.remove(x)
                                l2.remove(x)
                            else:
                                print(2)
                                x=random.choice(l2)
                                print(x)
                                l2.remove(x)

                        else:
                            x=random.choice(l2)
                            l2.remove(x)
                            if x in l3:
                                l3.remove(x)

                else:
                    x=j
                    l2.remove(x)
                    if x in l3:
                        l3.remove(x)

                for i in range(3):
                    for j in range(3):
                        if l1[i][j]==x:
                            l[i][j]='o'

                print(l[0][0]," | ",l[0][1]," | ",l[0][2])
                print("------------------")
                print(l[1][0]," | ",l[1][1]," | ",l[1][2])
                print("------------------")
                print(l[2][0]," | ",l[2][1]," | ",l[2][2])
                print()
                print()


                print(f"I have put o at {x}")

                k=check_1(l)
                if k=='x':
                    print("You won!!")
                    break
                elif k=='o':
                    print("I won!!")
                    break
                elif k=='':
                    if l2==[]:
                        print("Draw!!")
                        break
        break

    elif n=='2':
        n1=input("What is the name of the player who has x?")
        n2=input("What is the name of the player who has o?")
        print(f"Therefore {n1} will start!")
        while True:
            while True:
                p1=input(f"Where do you want to put x,{n1}?")
                if p1 in l2:
                    for i in range(3):
                        for j in range(3):
                            if l1[i][j]==p1:
                                l[i][j]='x'
                                l2.remove(p1)
                    break
                else:
                    print("Invalid Input!")
                    continue

            print(l[0][0]," | ",l[0][1]," | ",l[0][2])
            print("------------")
            print(l[1][0]," | ",l[1][1]," | ",l[1][2])
            print("------------")
            print(l[2][0]," | ",l[2][1]," | ",l[2][2])
            print()
            print()

            k=check_1(l)
            if k=='o':
                print(f"{n2} won!!")
                break
            elif k=='x':
                print(f"{n1} won!!")
                break
            elif k=='':
                if l2==[]:
                    print("Draw!!")
                    break
                
            while True:
                p2=input(f"Where do you want to put o,{n2}?")
                if p2 in l2:
                    for i in range(3):
                        for j in range(3):
                            if l1[i][j]==p2:
                                l[i][j]='o'
                                l2.remove(p2)
                    break
                else:
                    print("Invalid Input!")
                    continue
            
            print(l[0][0]," | ",l[0][1]," | ",l[0][2])
            print("------------")
            print(l[1][0]," | ",l[1][1]," | ",l[1][2])
            print("------------")
            print(l[2][0]," | ",l[2][1]," | ",l[2][2])
            print()
            print()
            
            k=check_1(l)
            if k=='o':
                print(f"{n2} won!!")
                break
            elif k=='x':
                print(f"{n1} won!!")
                break
            elif k=='':
                if l2==[]:
                    print("Draw!!")
                    break

    else:
        print("Only 1 or 2 players can play :)")
        continue
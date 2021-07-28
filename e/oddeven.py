import random

print("Let's play Tic-Tac-Toe!!!")
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

def check(list):
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

if c=='x':
    print("I will start!")
    while True:    
        x=random.choice(l2)

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
        l2.remove(x)

        k=check(l)
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

        k=check(l)
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

elif p=='x':
    print("You will start!")    
    while True:
        while True:
            x1=str(input("Where do you want to put x?"))
            if x1 not in l2:
                print("Invalid input")
                continue
            else:
                break
        l2.remove(x1)

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

        k=check(l)
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
        
        x=random.choice(l2)

        for i in range(3):
            for j in range(3):
                if l1[i][j]==x:
                    l[i][j]='o'

        print(l[0][0]," | ",l[0][1]," | ",l[0][2])
        print("------------")
        print(l[1][0]," | ",l[1][1]," | ",l[1][2])
        print("------------")
        print(l[2][0]," | ",l[2][1]," | ",l[2][2])
        print()
        print()

        print(f"I have put o at {x}")
        l2.remove(x)

        k=check(l)
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
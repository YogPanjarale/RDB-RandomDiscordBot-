import random
print("Let's play Rock, Paper and Scissors. Can you beat me!?")
print("For your convenience you can write r for rock, p for paper and s for scissors :)")
print("And don't worry I will count our scores.")

CSetScore=0
PSetScore=0

rps=['r','p','s']
d={'r':0, 'p':0, 's':0}

z=int(input("You want to play best of "))
z1=z//4

i=1
while i<=z:
    CScore=0
    PScore=0  
    x1=input("What's your move? ")
    x=x1.lower()

    if i in range(1,z1):
        d[x]+=1
        y=random.choice(rps)
        print(d)
    else:
        if i%2==0:
            k=max(d.values())
            for j in d.keys():
                if d[str(j)]==k:
                    if str(j)=='r':
                        y='p'
                    elif str(j)=='p':
                        y='s'
                    elif str(j)=='s':
                        y='r'
        else:
            y=random.choice(rps)
    
    print("My move is",y)
    if x=='r':
        if y=='r':
            print(":|")
        elif y=='p':
            print(":)")
            CScore+=1
        elif y=='s':
            print(":(")
            PScore+=1
    elif x=='p':
        if y=='r':
            print(":(")
            PScore+=1
        elif y=='p':
            print(":|")
        elif y=='s':
            print(":)")
            CScore+=1
    elif x=='s':
        if y=='r':
            print(":)")
            CScore+=1
        elif y=='p':
            print(":(")
            PScore+=1
        elif y=='s':
            print(":|")
    
    if CScore>PScore:
        CSetScore+=1
    elif PScore>CScore:
        PSetScore+=1
        
    i+=1

print("My score is",CSetScore)
print("Your score is",PSetScore)
if CSetScore>PSetScore:
    print("I WON!! Better luck next time.")
elif PSetScore>CSetScore:
    print("Congrats!! YOU WON!!")
else:
    print("DRAW!!!")

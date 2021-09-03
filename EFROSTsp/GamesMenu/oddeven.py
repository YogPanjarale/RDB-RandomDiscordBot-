import random
def odd_even():
    print("Let's play cricket without bat and ball!!!")
    print("Yeah! You guessed it we are playing odd even.")
    print("Don't worry I count our scores.")

    while True:
        player1=input("So what do you choose odd or even? ")
        player=player1.lower()
        comp=''
        if player=='odd':
            print("Good then I have even!")
            comp='even'
            break
        elif player=='even':
            print("Good then I have odd!")
            comp='odd'
            break
        else:
            print("Please type what is asked, don't be oversmart! Sorry if I'm rude.")
            continue

    numbers=[1,2,3,4,5,6,7,8,9,10]
    print("Let's decide who will bat first and ball first.")
    while True:
        x=int(input("Your move:"))
        if x in numbers:
            break
        else:
            print("Invalid input")
            continue
    y=random.randint(1,10)
    print("My move is",y)
    Player=''
    Comp=''
    if (x+y)%2==0:
        if player=='odd':
            print("It's even that means I win :)")
            z=random.choice(["Bat","Ball"])
            print(f"Therefore I choose to {z} first")
            Comp=z
            for i in ("Bat","Ball"):
                if i!=z:
                    print(f"That means you have {i}")
                    Player=i
        else:
            print("It's even that means you win :(")
            while True:
                z1=input("What do you choose? ")
                if z1 in ('bat','ball','Bat','Ball'):
                    if z1[0]=='b':
                        z2=z1.replace('b','B')
                    else:
                        z2=z1
                    break
                else:
                    print("Invalid input")
                    continue
            Player=z2
            for i in (["Bat","Ball"]):
                if i!=z2:
                    print(f"That means I have {i}")
                    Comp=i
    else:
        if player=='even':
            print("It's odd that means I win :)")
            z=random.choice(["Bat","Ball"])
            print(f"Therefore I choose to {z} first")
            Comp=z
            for i in ("Bat","Ball"):
                if i!=z:
                    print(f"That means you have {i}")
                    Player=i
        else:
            print("It's odd that means you win :(")
            while True:
                z1=input("What do you choose? ")
                if z1 in ('bat','ball','Bat','Ball'):
                    if z1[0]=='b':
                        z2=z1.replace('b','B')
                    else:
                        z2=z1
                    break
                else:
                    print("Invalid input")
                    continue
            Player=z2
            for i in ("Bat","Ball"):
                if i!=z2:
                    print(f"That means I have {i}")
                    Comp=i

    print("Let's start!")

    if Player=="Bat" and Comp=="Ball":
        PlayerScore=0
        CompScore=0
        
        d={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0}
        l=[]
        count=0

        while True:    
            while True:
                while True:
                    x=int(input("Your move:"))
                    if x not in numbers:
                        print("Invalid input")
                        continue
                    else:
                        break
                if x in numbers:
                    l.append(str(x))
                    d[str(x)]+=1
                    count+=1
                    if count>10:
                        for i in d.keys():
                            d[str(l[count-11])]-=1
                    break
                else:
                    print("Invalid input")
                    continue
            if count>10:
                if count%2==0:
                    m=max(d.values())
                    for i in d.keys():
                        if d[i]==m:
                            y=int(i)
                else:
                    y=random.randint(1,10)
            else:
                y=random.randint(1,10)
            print("My move:",y)
            if x==y:
                print("Out!!")
                print("Your score is",PlayerScore,".")
                print("My turn to bat and I need",PlayerScore+1,"runs to win.")
                break
            else:
                PlayerScore+=x
        
        d={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0}
        l=[]
        count=0
        
        while True:
            while True:
                while True:
                    x=int(input("Your move:"))
                    if x not in numbers:
                        print("Invalid input")
                        continue
                    else:
                        break
                if x in numbers:
                    l.append(str(x))
                    d[str(x)]+=1
                    count+=1
                    if count>10:
                        for i in d.keys():
                            d[str(l[count-11])]-=1
                    break
                else:
                    print("Invalid input")
                    continue
            if count>10:
                if count%2==0:
                    m=min(d.values())
                    for i in d.keys():
                        if d[i]==m:
                            y=int(i)
                else:
                    y=random.randint(1,10)
            else:
                y=random.randint(1,10)
            print("My move:",y)
            if x==y:
                print("Out!!")
                break
            else:
                CompScore+=y
                if CompScore>PlayerScore:
                    print("My score is",CompScore)
                    print("I WON!! Better luck next time :)")
                    break

        if CompScore==PlayerScore:
            print("My score is",CompScore)
            print("The match tied!!!")
        elif CompScore<PlayerScore:
            print("My score is",CompScore)
            print("Congrats!!You WON!!")

    else:
        PlayerScore=0
        CompScore=0

        d={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0}
        l=[]
        count=0

        while True:    
            while True:
                while True:
                    x=int(input("Your move:"))
                    if x not in numbers:
                        print("Invalid input")
                        continue
                    else:
                        break
                if x in numbers:
                    l.append(str(x))
                    d[str(x)]+=1
                    count+=1
                    if count>10:
                        for i in d.keys():
                            d[str(l[count-11])]-=1
                    break
                else:
                    print("Invalid input")
                    continue
            if count>10:
                if count%2==0:
                    m=min(d.values())
                    for i in d.keys():
                        if d[i]==m:
                            y=int(i)
                else:
                    y=random.randint(1,10)
            else:
                y=random.randint(1,10)
            print("My move:",y)
            if x==y:
                print("Out!!")
                print("My score is",CompScore,".")
                print("Your turn to bat and you need",CompScore+1,"runs to win.")
                break
            else:
                CompScore+=y
        
        d={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0}
        l=[]
        count=0

        while True:
            while True:
                while True:
                    x=int(input("Your move:"))
                    if x not in numbers:
                        print("Invalid input")
                        continue
                    else:
                        break
                if x in numbers:
                    l.append(str(x))
                    d[str(x)]+=1
                    count+=1
                    if count>10:
                        for i in d.keys():
                            d[str(l[count-11])]-=1
                    break
                else:
                    print("Invalid input")
                    continue
            if count>10:
                if count%2==0:
                    m=max(d.values())
                    for i in d.keys():
                        if d[i]==m:
                            y=int(i)
                else:
                    y=random.randint(1,10)
            else:
                y=random.randint(1,10)
            print("My move:",y)
            if x==y:
                print("Out!!")
                break
            else:
                PlayerScore+=x
                if PlayerScore>CompScore:
                    print("Your score is",PlayerScore)
                    print("You WON!!")
                    break
                
        if CompScore==PlayerScore:
            print("Your score is",PlayerScore)
            print("The match tied!!!")
        elif CompScore>PlayerScore:
            print("Your score is",PlayerScore)
            print("I WON!! Better luck next time :)")

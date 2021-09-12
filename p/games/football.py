import random
def fb():
    print("Let's play football without football!!!")

    while True:
        x=input("Choose foot or ball>")
        if x=='foot':
            print("Therefore I have ball!")
            break
        elif x=='ball':
            print("Therefore I have foot!")
            break
        else:
            print("Invalid Input!!")
            continue

    n=int(input("Enter a number between 1 to 10:"))
    n1=random.randint(1,10)
    print("I took out",n1)

    pl=''
    cm=''

    pgoals=0
    cgoals=0

    if x.lower()=='foot':
        if (n+n1)%2==0:
            r=random.choice(['Center','Side'])
            print(f"I won, therefore I choose {r}!!")
            for i in ['Center','Side']:
                if i!=r:
                    print(f"Therefore you have {i}!!")
            if r=='Center':
                cm='ball'
            else:
                pl='ball'
        else:
            print("You won!!")
            y=input("Choose center or side>")
            if y.lower()=='center':
                print("Therfore I have side!!")
                pl='ball'
            elif y.lower()=='side':
                print("Therefore I have center!!")
                cm='ball'
    else:
        if (n+n1)%2==0:
            print("You won!!")
            y=input("Choose center or side>")
            if y.lower()=='center':
                print("Therfore I have side!!")
                pl='ball'
            elif y.lower()=='side':
                print("Therefore I have center!!")
                cm='ball'
        else:
            r=random.choice(['Center','Side'])
            print(f"I won, therefore I choose {r}!!")
            for i in ['Center','Side']:
                if i!=r:
                    print(f"Therefore you have {i}!!")
            if r=='Center':
                cm='ball'
            else:
                pl='ball'

    print("Let's start the match!!!")

    t=int(input("For how many goals do you want to play?"))
    n=0
    while True:
        n+=1
        p=int(input("Enter number:"))
        if p not in [1,2,3]:
            while True:
                print("PENELTY!!!")
                print("Enter 7, 8 or 9!!")
                k=int(input("Enter number:"))
                if k not in (7,8,9):
                    continue
                else:
                    r=random.randint(7,9)
                    print("My number:",r)
                    if k==r:
                        print("Goal Saved!!")
                    else:
                        print("GOAL!!!")
                        cgoals+=1
                    print("Your Score:",pgoals)
                    print("My Score:",cgoals)
                    pl,cm=cm,pl
                    if pgoals!=t and cgoals!=t:
                        if pl=='ball':
                            print("You have the ball now!!")
                        else:
                            print("I have the ball now!!")
                    n=0
                    break
            continue
        
        c=random.randint(1,3)
        print("My number:",c)

        if p!=c:
            print(f"Pass {n}")
            if n!=3:
                continue
        else:
            print("Tackled!!")
            n=0
            pl,cm=cm,pl
            if pl=='ball':
                print("You have the ball now!!")
            else:
                print("I have the ball now!!")
            continue

        if n==3:
            print("Goal Time!!")
            print("Enter 4, 5 or 6!!")
            g=int(input("Enter number:"))
            if g not in (4,5,6):
                while True:
                    print("PENELTY!!!")
                    print("Enter 7, 8 or 9!!")
                    k=int(input("Enter number:"))
                    if k not in (7,8,9):
                        continue
                    else:
                        r=random.randint(7,9)
                        print("My number:",r)
                        if k==r:
                            print("Goal Saved!!")
                        else:
                            print("GOAL!!!")
                            cgoals+=1
                        print("Your Score:",pgoals)
                        print("My Score:",cgoals)
                        pl,cm=cm,pl
                        if pgoals!=t and cgoals!=t:
                            if pl=='ball':
                                print("You have the ball now!!")
                            else:
                                print("I have the ball now!!")
                        n=0
                        break
                continue
            else:
                r=random.randint(4,6)
                print("My number:",r)
                if g==r:
                    print("Goal Saved!!")
                else:
                    print("GOAL!!!")
                    if pl=='ball':
                        pgoals+=1
                    else:
                        cgoals+=1
                print("Your Score:",pgoals)
                print("My Score:",cgoals)
                pl,cm=cm,pl
                if pgoals!=t and cgoals!=t:
                    if pl=='ball':
                        print("You have the ball now!!")
                    else:
                        print("I have the ball now!!")

        if pgoals==t:
            print("YOU WON!!!")
            break
        elif cgoals==t:
            print("I WON!!!")
            break
        
        n=0
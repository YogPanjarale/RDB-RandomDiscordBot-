import random
def snakes_and_ladders():
    player=1
    ai=1
    ladder={4:14,9:31,20:38,28:84,40:59,51:67,63:81,71:91}
    snake={17:7,54:34,62:19,64:60,87:24,93:73,95:75,99:78}

    i=0

    while player<=100 and ai<=100:    
        if i%2==0:
            print("PLAYER'S TURN")
            while True:
                x=input("Write roll:")
                if x.lower()=="roll":
                    dice=random.randint(1,6)
                    break
                else:
                    print("Write roll!")
                    continue
            if dice==6:
                i+=0
            else:
                i+=1
            print("Dice:",dice)
            player+=dice
            if player>100:
                player-=dice
                i+=0
                print("Player:",player)
                continue
            print("Player:",player)
            if player in ladder.keys():
                player=ladder[player]
                print("Player has took a ladder and reached",player)
            elif player in snake.keys():
                player=snake[player]
                print("Player has been bitten by a snake and reached",player)
            elif player==100:
                print('PLAYER WIN!')
                break
        else:
            print("AI'S TURN")
            dice=random.randint(1,6)
            if dice==6:
                i+=0
            else:
                i+=1
            print("Dice:",dice)
            ai+=dice
            if ai>100:
                ai-=dice
                i+=0
                print("AI:",ai)
                continue
            print("AI:",ai)
            if ai in ladder.keys():
                ai=ladder[ai]
                print("AI has took a ladder and reached",ai)
            elif ai in snake.keys():
                ai=snake[ai]
                print("AI has been bitten by a snake and reached",ai)
            elif ai==100:
                print('AI WIN!')
                break
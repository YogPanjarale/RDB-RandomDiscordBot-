import random 
cards = {'A ':1,'2 ':2,'3 ':3,'4 ':4,'5 ':5,'6 ':6,'7 ':7,'8 ':8,'9 ':9,'10':10,'J ':10,'Q ':10,'K ':10}
card_list = ['A ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10', 'J ', 'Q ', 'K ']
player_cards=[]
AI_cards=[]
a = random.choice(card_list)
b = random.choice(card_list)
aa = cards[f"{a}"]
bb = cards[f"{b}"]
e = random.choice(card_list)
f = random.choice(card_list)
ee = cards[f"{e}"]
ff = cards[f"{f}"]
AI_cards.append(e)
AI_cards.append(f)
player_cards.append(a)
player_cards.append(b)
print()
print("The computer will be the dealer here , you are just required to enter hit or st (stand) whenever you get your cards")
print(f"+------+  +------+\n| {a}   |  | {b}   |\n|      |  |      |  \n|      |  |      |  \n|      |  |      |\n|    {a}|  |    {b}|\n+------+  +------+")
print("Your total points with these cards are -",bb+aa)
print(f"+------+  +------+\n| {e}   |  | {f}   |\n|      |  |      |  \n|      |  |      |  \n|      |  |      |\n|    {e}|  |    {f}|\n+------+  +------+")
print("AI's total points with these cards are -",ee+ff)
jj=21-(aa+bb)
print()
print(f"You are {jj} point(s) away from getting a blackjack")
print()
wtd = input("what would you like to do ?")
if wtd=='hit':
    c = random.choice(card_list)
    cc = cards[f"{c}"]
    k = random.choice(card_list)
    kk = cards[f"{k}"]
    print(f"+------+  +------+  +------+\n| {a}   |  | {b}   |  | {c}   |\n|      |  |      |  |      |\n|      |  |      |  |      |\n|      |  |      |  |      |\n|    {a}|  |    {b}|  |    {c}|\n+------+  +------+  +------+")
    print(f"+------+  +------+  +------+\n| {e}   |  | {f}   |  | {k}   |\n|      |  |      |  |      |\n|      |  |      |  |      |\n|      |  |      |  |      |\n|    {e}|  |    {f}|  |    {k}|\n+------+  +------+  +------+")  
    print("Your total points with these cards are -",bb+aa+cc)
    if bb+aa+cc>=21:
        print("BUST,sorry, the dealer gets the money")
    else:
        print("its the AIs turn now")
elif wtd=='st':
    print("its the AIs turn now")

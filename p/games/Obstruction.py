import random
def obstr():
    obs = {'a1':'a2,b2,b1','a2':'a1,a3,b1,b2,b3','a3':'a2,a4,b2,b3,b4','a4':'a3,a5,b3,b4,b5','a5':'a4,a6,b4,b5,b6','a6':'a5,b5,b6',
        'b1':'a1,a2,b2,c2,c1','b2':'a1,a2,a3,b1,b3,c1,c2,c3','b3':'a2,a3,a4,b2,b4,c2,c3,c4','b4':'a3,a4,a5,b3,b5,c3,c4,c5','b5':'a4,a5,a6,b4,b6,c4,c5,c6','b6':'a6,a5,b5,c5,c6',
        'c1':'b1,b2,c2,d1,d2','c2':'b1,b2,b3,c1,c3,d1,d2,d3','c3':'b2,b3,b4,c2,c4,d2,d3,d4','c4':'b3,b4,b5,c3,c5,d3,d4,d5','c5':'b4,b5,b6,c4,c6,d4,d5,d6','c6':'b6,b5,c5,d5,d6',
        'd1':'c1,c2,d2,e1,e2','d2':'d1,c2,c3,c1,d3,e1,e2,e3','d3':'c2,c3,c4,d2,d4,e2,e3,e4','d4':'c3,c4,c5,d3,d5,e3,e4,e5','d5':'c4,c5,c6,d4,d6,e4,e5,e6','d6':'c6,c5,d5,e5,e6',
        'e1':'d1,d2,e2,f1,f2','e2':'d1,d2,d3,e1,e3,f1,f2,f3','e3':'d2,d3,d4,e2,e4,f2,f3,f4','e4':'d3,d4,d5,e3,e5,f3,f4,f5','e5':'d4,d5,d6,e4,e6,f4,f5,f6','e6':'d6,d5,e5,f5,f6',
        'f1':'e1,e2,f2','f2':'f1,e1,e2,e3,f3','f3':'f2,e2,e3,e4,f4','f4':'f3,e3,e4,e5,f5','f5':'f4,e4,e5,e6,f6','f6':'f5,e5,e6'}
    l1=['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6','c1','c2','c3','c4','c5','c6','d1','d2','d3','d4','d5','d6','e1','e2','e3','e4','e5','e6','f1','f2','f3','f4','f5','f6']
    l2=['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6','c1','c2','c3','c4','c5','c6','d1','d2','d3','d4','d5','d6','e1','e2','e3','e4','e5','e6','f1','f2','f3','f4','f5','f6']
    print("Its the players turn")
    print()
    print("+------+------+------+------+------+------+")
    print("| ",l1[0]," | ",l1[1]," | ",l1[2]," | ",l1[3]," | ",l1[4]," | ",l1[5]," |")
    print("+------+------+------+------+------+------+")
    print("| ",l1[6]," | ",l1[7]," | ",l1[8]," | ",l1[9]," | ",l1[10]," | ",l1[11]," |")
    print("+------+------+------+------+------+------+")
    print("| ",l1[12]," | ",l1[13]," | ",l1[14]," | ",l1[15]," | ",l1[16]," | ",l1[17]," |")
    print("+------+------+------+------+------+------+")
    print("| ",l1[18]," | ",l1[19]," | ",l1[20]," | ",l1[21]," | ",l1[22]," | ",l1[23]," |")
    print("+------+------+------+------+------+------+")
    print("| ",l1[24]," | ",l1[25]," | ",l1[26]," | ",l1[27]," | ",l1[28]," | ",l1[29]," |")
    print("+------+------+------+------+------+------+")
    print("| ",l1[30]," | ",l1[31]," | ",l1[32]," | ",l1[33]," | ",l1[34]," | ",l1[35]," |")
    print("+------+------+------+------+------+------+")
    print()
    while True:
        if len(l2)==0:
            print("You have lost to the AI in a fair match , lol")
            break  
        else:
            x=input("Where do you want to put the X? , look at the grid and enter accordingly: \n")
            aa = obs[f'{x}']
            if x in l2:
                l2.remove(x)
                bb = aa.split(',')
                a = str(l1).replace(f'{x}','XX')
                b = str(a).replace("'",'') 
                c = str(b).replace('[','')
                d = str(c).replace(']','')
                e = str(d).replace(" ","")

                for j in bb:
                    if j in e:
                        l2.remove(j)
                        e = e.replace(j,"//")
                        continue
                l1=e.split(',')
                print("+------+------+------+------+------+------+")
                print("| ",l1[0]," | ",l1[1]," | ",l1[2]," | ",l1[3]," | ",l1[4]," | ",l1[5]," |")
                print("+------+------+------+------+------+------+")
                print("| ",l1[6]," | ",l1[7]," | ",l1[8]," | ",l1[9]," | ",l1[10]," | ",l1[11]," |")
                print("+------+------+------+------+------+------+")
                print("| ",l1[12]," | ",l1[13]," | ",l1[14]," | ",l1[15]," | ",l1[16]," | ",l1[17]," |")
                print("+------+------+------+------+------+------+")
                print("| ",l1[18]," | ",l1[19]," | ",l1[20]," | ",l1[21]," | ",l1[22]," | ",l1[23]," |")
                print("+------+------+------+------+------+------+")
                print("| ",l1[24]," | ",l1[25]," | ",l1[26]," | ",l1[27]," | ",l1[28]," | ",l1[29]," |")
                print("+------+------+------+------+------+------+")
                print("| ",l1[30]," | ",l1[31]," | ",l1[32]," | ",l1[33]," | ",l1[34]," | ",l1[35]," |")
                print("+------+------+------+------+------+------+")
            else:
                print("illegal move : that Grid element is already occupied")
                print("Your turn is now skipped for that")
        if len(l2)==0:
            print("The AI has lost in a fair match , GG")
            break 
        else:
            z = random.choice(l2)
            nn = obs[f'{z}']
            l2.remove(z)
            mm = nn.split(',')
            p = str(l1).replace(f'{z}','OO')
            q = str(p).replace("'",'') 
            r = str(q).replace('[','')
            s = str(r).replace(']','')
            t = str(s).replace(" ","")
            for u in mm:
                if u in t:
                    l2.remove(u)
                    t = t.replace(u,"::")
                    continue
            l1=t.split(',')
            print()
            print("+------+------+------+------+------+------+")
            print("| ",l1[0]," | ",l1[1]," | ",l1[2]," | ",l1[3]," | ",l1[4]," | ",l1[5]," |")
            print("+------+------+------+------+------+------+")
            print("| ",l1[6]," | ",l1[7]," | ",l1[8]," | ",l1[9]," | ",l1[10]," | ",l1[11]," |")
            print("+------+------+------+------+------+------+")
            print("| ",l1[12]," | ",l1[13]," | ",l1[14]," | ",l1[15]," | ",l1[16]," | ",l1[17]," |")
            print("+------+------+------+------+------+------+")
            print("| ",l1[18]," | ",l1[19]," | ",l1[20]," | ",l1[21]," | ",l1[22]," | ",l1[23]," |")
            print("+------+------+------+------+------+------+")
            print("| ",l1[24]," | ",l1[25]," | ",l1[26]," | ",l1[27]," | ",l1[28]," | ",l1[29]," |")
            print("+------+------+------+------+------+------+")
            print("| ",l1[30]," | ",l1[31]," | ",l1[32]," | ",l1[33]," | ",l1[34]," | ",l1[35]," |")
            print("+------+------+------+------+------+------+")
            print()  
            continue 

        





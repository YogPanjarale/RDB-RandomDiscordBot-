import random
d={'q':'a','a':'z','z':'q','w':'s','s':'x','x':'w','e':'d','d':'c','c':'e','r':'f','f':'v','v':'r','t':'g','g':'b','b':'t','y':'h','h':'n','n':'y','u':'j','j':'m','m':'u','i':'k','k':'i','o':'l','l':'o','p':'p'}
D={'Q':'A','A':'Z','Z':'Q','W':'S','S':'X','X':'W','E':'D','D':'C','C':'E','R':'F','F':'V','V':'R','T':'G','G':'B','B':'T','Y':'H','H':'N','N':'Y','U':'J','J':'M','M':'U','I':'K','K':'I','O':'L','L':'O','P':'P'}
n={'1':')','2':'(','3':'*','4':'&','5':'^','6':'%','7':'$','8':'#','9':'@','0':'!'}
while True:
    print("You can write 'no' if you don't want to encrypt or decrypt.")
    z=input("Do you want to encrypt or decrypt?")
    if z.lower()=="e":
        x = input("Enter the something to be encrypted: ")
        y=''
        for i in x:
            if i.isupper():
                y+=D[i]
            elif i.islower():
                y+=d[i]
            elif i==' ':
                y+='-'
            elif i.isnumeric():
                y+=n[i]
            else:
                if i in n.values():
                    for k in n.keys():
                        if n[k]==i:
                            y+=str(k)
                elif i==',':
                    y+='.'
                elif i=='.':
                    y+=','
                elif i=='?':
                    y+='|'
                else:
                    y+=i
        print(y)
        l=list(y)
        print(l)
        random.shuffle(l)
        y1= ''.join(l)
        print(y1)
        continue
    elif z.lower()=='d':
        c=input("Enter the something to be decrypted: ")
        if c==y1:
            a=y
        b=''
        for i in a:
            if i.isupper():
                for j in D.keys():
                    if i==D[j]:
                        b+=j
            elif i.islower():
                for j in d.keys():
                    if i==d[j]:
                        b+=j
            elif i=='-':
                b+=' '
            elif i in n.values():
                for k in n.keys():
                    if n[k]==i:
                        b+=str(k)
            elif i.isnumeric():
                b+=n[i]
            elif i=='.':
                b+=','
            elif i==',':
                b+='.'
            elif i=='|':
                b+='?'
            else:
                b+=i
        print(b)
        continue

    elif z.lower()=='no':
        break   
    else:
        print("Invalid input!")
        continue
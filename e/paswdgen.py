import random
x = input("enter the message to be encrypted: \n")
y=x.lower()
l=list(y)
k = ['f','g','h','j','k','l','a','s']
m = ['q','w','e','r','t','y','u','i']
dd = random.choice(k)
mm = random.choice(m)
random.shuffle(l)
c = ''.join(l)
f=''
a=['a','c','e','g','i','k','m','o','q','s','u','w','y']
b=['b','d','f','h','j','l','n','p','r','t','v','x','z']
for i in c:
    if i in a:
        f+=f"{dd}"
    elif i in b:
        f+=f"{mm}"
    elif i==" ":
        f+='-'
    else:
        print("error")
print(f) 
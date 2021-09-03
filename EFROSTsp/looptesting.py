import os
a = ['a','b','c','d']
b = ['g','k','c','h','b','e','a','d']
aa = str(b)
for i in a:
    if i in b:
        aa = aa.replace(i,"#")
        continue
 
list(aa)
print(aa)
#d = os.listdir('/home/pi/rdb/python')
#for k in d:
    #print(k)
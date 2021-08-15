import os
name = input("enter a file name:\n")
fname = '/home/pi/rdb/r/'+name
f = open(f"{fname}",'r')
b = f.read(2000)
print(b)


    


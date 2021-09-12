row=int(input("Enter number of rows:"))
col=int(input("Enter number of coloums:"))
l=[]
for i in range(row):
    for j in range(col):
        l.append(f'l{i+1}{j+1}')

for i in range(row):
    print('+',end='')
    print('-----+'*col)
    print('|',end='')
    for j in range(col):
        print(f' l{i+1}{j+1} |',end='')
    print()
print('+',end='')
print('-----+'*col) 
print()
print(l)
print()
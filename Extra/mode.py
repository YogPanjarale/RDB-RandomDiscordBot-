from collections import Counter
from time import sleep
print('lets play odd even')
a = input("what do u choose? - type o or e: \n")

n_num =[]
while True:
    no = int(input("enter a few numbers: \n"))
    n_num.append(no)
    if len(n_num)==10:
        break
n = len(n_num)
  
data = Counter(n_num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
  
if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is / are: " + ', '.join(map(str, mode))
      
print(get_mode)
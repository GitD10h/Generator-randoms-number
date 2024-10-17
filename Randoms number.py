import random
import time
print('Input random numbers: ')
a = int(input())
print('Input random numbers, which more start.')
b = int(input())
if a >= b:
    print('Eror')
else:    
    c = random.randint(a, b)
    print(c)
    t = time.localtime(time.time())
    localtime = time.asctime(t)
    str = "Current Time:" + time.asctime(t)
    print(str)

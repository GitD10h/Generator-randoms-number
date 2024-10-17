import random

print('Input random numbers: ')
a = int(input())
print('Input random numbers, which more start.')
b = int(input())
if a >= b:
    print('Eror')
else:    
    c = random.randint(a, b)
    print(c)
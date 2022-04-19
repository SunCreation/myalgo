from time import time



def hi(num):
    n = 0 
    while n < num:
        yield n
        n += 1

st = time()
for i in hi(100000):
    a=  0
    a += 1
print(time() -st)



st = time()

for i in range(100000):
    a = 0
    a += 1
print(time() -st)
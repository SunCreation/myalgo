N = 1000000 # int(input())
from time import time

st = time()

prime = set(range(2,N+1))

for i in range(2,int(N**0.5)+1):
    if i in prime:
        prime -= set(range(2*i,N+1,i))

print(prime, len(prime), st - time())

# for i in prime:
#     for j in range(2,i):
#         if i%j==0:
#             print('실패!')

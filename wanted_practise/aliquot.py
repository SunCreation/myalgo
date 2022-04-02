
#3 3
#2 4
#5 2
# 2  3  5
# 0  0  0
# 1  1  1
# 2  2  2
# 3  3
# 4
# (1 + 2 + 2**2 + 2**3 + 2**4)(1 + 3 + 3**2 + 3**3)(1 + 5 + 5**2)

from collections import defaultdict
from time import time
N = int(input())

aliquot = [0]*(N+1)
prime = set(range(2,N+1))
for i in range(2,int(N**0.5)+1):
    if i in prime:
        prime -= set(range(2*i,N+1,i))

def f(num, goal=None):
    if not goal: 
        goal=num
        aliquot[goal] = defaultdict(int)
    if num in prime:
        aliquot[goal][num] += 1
        return
    for i in prime:
        if num % i == 0:
            aliquot[goal][i] += 1
            if aliquot[num//i]:
                # print('good!!')
                for j,k in aliquot[num//i].items():
                    aliquot[goal][j] += k
                return
            else:
                f(num//i, goal)
                return 
    
    # aliquot[goal][num] += 1
def aliquot_sum(num):
    total = 1
    for i,j in aliquot[num].items():
        total *= sum([i**n for n in range(j+1)])
    return total

st = time()
total = 0
for i in range(1,N+1):
    f(i)
    total += aliquot_sum(i)


# f(N)

print(total, time() - st)
# 한자리 숫자가 적힌 종이 조각이 
# 무튼 숫자들을 다 
# 이거 풀어서 뭐 할 수 있는걸까?
from itertools import permutations

def solution(numbers):
    nums = {''.join(i) for i in permutations(numbers)}

    mx=int(''.join(max(nums)))
    primes = {2} | {i for i in range(3,mx+1,2)}
    for i in range(3,int(mx**0.5)+2):
        primes -= set(range(2*i,mx + 1, i))
        
    answer = 0
    for i in range(1,len(numbers)):
        nums |= {''.join(i) for i in permutations(numbers,i)}
        
    for i in set(map(int,nums)):
        if i in primes:
            answer += 1
    return answer
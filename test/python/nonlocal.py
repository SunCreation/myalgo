import re
a = "100-200*300-500+20"
def go(exp, op):
    return re.search('[\d]+\*[\d]+', exp)


go(a,'*')





from itertools import permutations
import re

def solution(expression):
    def go(exp, op):
        return re.search(f'\(*\-*[\d]+\)*\\{op}\(*\-*[\d]+\)*', exp)
        
    result = []
    for i in permutations('+-*',3):
        run = expression
        for j in i:
            while pos := go(run,j):
                run = run[:pos.start()]+'('+str(eval(run[pos.start():pos.end()]))+')'+run[pos.end():]
        result.append(str(abs(int(run))))
    answer = max(result)
    return answer
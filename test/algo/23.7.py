import sys
from pprint import pprint

sys.stdin = open('data/23.7','r')

col, row = map(int, input().split())

matrix = []
for i in range(col):
    matrix.append(list(input()))

# pprint(matrix)

def check(now):
    x,y = now
    if matrix[x][y]=='*':
        return
    checklist = [(x,y+1),(x,y-1),(x-1,y),(x+1,y),(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1)]
    count = 0

    for i,j in checklist:
        if i in range(col) and j in range(row) and matrix[i][j]=='*':
            count += 1
    matrix[x][y] = str(count)
#---------------------------
for i in range(col):
    for j in range(row):
        check((i,j))

pprint(matrix)

# for i in matrix:
#     print(''.join(i))
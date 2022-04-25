import sys

checklist = ['dz=','nj','lj','c=','c-','d-','s=','z=']
def numcheck(s):
    for i in checklist:
        s = s.replace(i, ':')
    
    return print(len(s))


with open('data/2941', 'r') as f:
    for i in f.readlines():
        s, n = i.split()
        if numcheck(s)==int(n):
            print('정답!!')
        else:
            print('땡!!')
            print(numcheck(s), n)


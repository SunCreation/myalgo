

from time import time

def howtime(f, *arg):
    st = time()

    print(f'함수값: {f(*arg)}')
    print(f'걸린 시간: {time() -st}초\n\n\n')

def which(lst, arg):
    return arg in lst


howtime(which,list(range(100000000)), 10000)
howtime(which,set(range(100000000)), 10000)
    
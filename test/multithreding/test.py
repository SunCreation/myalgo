from time import time

num_list = ['p1','p2','p3','p4']*4

start = time()

def count(name):
    for i in range(100000000):
        a = 1 + 2

    print('finish:'+name+"\n")

for i in num_list:
    count(i)

print('time:', time() -start)


from multiprocessing import Pool
start = time()

if __name__=='__main__':
    pool = Pool(processes=16)
    pool.map(count, num_list)
    pool.close()
    pool.join()

print('time:', time() -start)




print('hi')


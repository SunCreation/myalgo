from time import time

num_list = [f'p{i}' for i in range(1,17)]

start = time()

def count(name):
    for i in range(100000000):
        a = 1 + 2

    print('finish:'+name+"\n")
    return name

# for i in num_list:
#     count(i)

# print('직렬 처리 time:', time() -start)



from multiprocessing import Pool
start = time()

if __name__=='__main__':
    pool = Pool(processes=16)
    pool.map(count, num_list)
    pool.close()
    output = pool.join()
    print(pool)

print('병렬 처리 time:', time() -start)




print('hi')


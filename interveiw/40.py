from collections import defaultdict, deque
times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2

timelist = [0]*N

tasks = deque([K-1])

timedict = defaultdict(list)
for i, j, k in times:
    timedict[i-1].append((j-1,k))
print(timedict)
while tasks:
    it  = tasks.popleft()
    for i, j in timedict[it]:
        time = timelist[it] + j
        if time < timelist[i] or not timelist[i]: timelist[i] = time
        tasks.append(i)
print(timelist)
if timelist.count(0)>1:
    print(-1)
else:
    print(max(timelist))




print(tasks)
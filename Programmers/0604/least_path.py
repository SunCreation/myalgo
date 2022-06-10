import sys
from pprint import pprint
from collections import deque
sys.stdin = open('data')

def solution(maps):
    h,w = len(maps),len(maps[0])
    now = 0, 0
    last = h-1, w-1
    i_task = deque([now])
    f_task = deque([last])
    
    x_set, y_set = set(range(h)),set(range(w))
    maps[h-1][w-1] = 4
    
    while i_task and f_task:
        x,y = i_task.popleft()
        pprint(maps)
        for nx, ny in ((x,y+1),(x,y-1),(x+1,y),(x-1,y)):
            if nx in x_set and ny in y_set: 
                if maps[nx][ny]==1: 
                    maps[nx][ny] = maps[x][y] + 1
                    i_task.append((nx,ny))
                elif maps[nx][ny]-maps[x][y]==4:
                    return maps[nx][ny]+maps[x][y]-3
                    
        x,y = f_task.popleft()
        pprint(maps)
        for nx, ny in ((x,y+1),(x,y-1),(x+1,y),(x-1,y)):
            if nx in x_set and ny in y_set: 
                if maps[nx][ny]==1: 
                    maps[nx][ny] = maps[x][y] + 1
                    f_task.append((nx,ny))
                elif maps[x][y]-maps[nx][ny]==2:
                    return maps[nx][ny]+maps[x][y]-3
    return -1


# # import sys
# # from pprint import pprint
# from collections import deque
# # sys.stdin = open('data')

# def solution(maps):
#     h,w = len(maps),len(maps[0])
#     now = 0,0
#     task = deque([now])
#     x_set, y_set = set(range(h)), set(range(w))

#     while task:
#         x,y = task.popleft()
#         for nx, ny in ((x,y+1),(x,y-1),(x+1,y),(x-1,y)):
#             if nx in x_set and ny in y_set and maps[nx][ny]==1: 
#                 maps[nx][ny] = maps[x][y]+1
#                 if (nx,ny)==(h-1,w-1):
#                     return maps[nx][ny]
#                 task.append((nx,ny))
#     return -1



# import sys
# from pprint import pprint
# from collections import deque
# sys.stdin = open('data')
# 이거 해보기
# def solution(maps):
#     h,w = len(maps),len(maps[0])
#     now = 0,0,1
#     task = deque([now])

#     while task:
#         x,y,count = task.popleft()
#         maps[x][y] = 2
#         for nx, ny in ((x,y+1),(x,y-1),(x+1,y),(x-1,y)):
#             if nx >= 0 and ny >= 0 and nx < h and ny < w and maps[nx][ny]==1: 
#                 if (nx,ny)==(h-1,w-1):
#                     return count+1
#                 task.append((nx,ny,count+1))
#     return -1

# # import sys
# # from pprint import pprint
# from collections import deque
# # sys.stdin = open('data')

# def solution(maps):
#     h,w = len(maps),len(maps[0])
#     now = 0,0
#     task = deque([now])

#     while task:
#         x,y = task.popleft()
#         for nx, ny in ((x,y+1),(x,y-1),(x+1,y),(x-1,y)):
#             if nx in range(h) and ny in range(w) and maps[nx][ny]==1: 
#                 task.append((nx,ny))
#                 maps[nx][ny] = maps[x][y] + 1
#                 # pprint(maps)
#                 if (nx,ny)==(h-1,w-1):
#                     return maps[nx][ny]
#     return -1

    # def look_around(now):
    #     x,y = now
    #     golist = ((x,y+1),(x+1,y),(x,y-1),(x-1,y))
    #     return [i for i in golist if i[0] in range(h) and i[1] in range(w) and maps[i[0]][i[1]]==1]
    
    # def count():
    #     count_ = 0
    #     for rows in maps:
    #         for num in rows:
    #             if num==2:
    #                 count_ +=1
    #     return count_

    # result = []
    # def dfs_go_around(now,maps):
    #     x,y = now
    #     # pprint(maps)
    #     maps[x][y]=2
    #     if (x,y)==(h-1,w-1):
    #         result.append(count())
    #         maps[x][y]=1
    #         return
    #     if len(hi:=look_around((x,y)))==0:
    #         maps[x][y]=1
    #         return
    #     for nx, ny in hi:
    #         dfs_go_around((nx,ny),maps)
    #     maps[x][y]=1
    now = 0,0
    # go_around(now)
    # print(maps)
    # print(result)
    
    # return min(result) if len(result)!=0 else -1


for q in sys.stdin.readlines():
    maps, answer = q.split()
    if solution(eval(maps))==eval(answer):
        print('정답!')
    else: print('땡!')

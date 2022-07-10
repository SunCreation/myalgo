# 아래와 같이 있다고 생각해보자.
# 1 0 0 1
# 2 0 0 2
# 1 1 1 0
# 0 2 0 1
# (a,b)좌표가 들어올 시 (a-1,b-1), (a-1,b), (a,b-1), (a,b) 네 위치를 확인하면 된다. 물론 범위 안에서만
#  확인했을 시 결과 -> (a-1,b-1),(a-1,b+1),(a+1,b-1),(a+1,b+1)
# 대각선을 확인해가며 좌표를 checklist에 모두 담는다.
# 이후 점들에서 겹치는게 있으면 fail! 매우 좋은 방법이라고 생각된다.

from itertools import permutations
from copy import deepcopy

def solution(grid):
    answer = []
    checklist = set()
    N = len(grid)

    def check_all(posis) -> bool:
        checklist.clear()
        for pos in zip(range(5),posis):
            if not check(pos): return False
        return True

    def check(now):
        task = [now]
        grid_ = deepcopy(grid)

        while task:
            x,y = task.pop()
            if (x,y) in checklist: return False
            checklist.add((x,y))
            
            if x-1 >= 0 and y-1 >= 0 and grid_[x-1][y-1]==0:
                task.append((x-1,y-1))
                grid_[x-1][y-1] = 2
            if x < N and y-1 >= 0 and grid_[x][y-1]==1:
                task.append((x+1,y-1))
                grid_[x][y-1] = 2
            if x-1 >= 0 and y < N and grid_[x-1][y]==1:
                task.append((x-1,y+1))
                grid_[x-1][y] = 2
            if x < N and y < N and grid_[x][y]==0:
                task.append((x+1,y+1))
                grid_[x][y] = 2
            print(task)
        return True

    for i in permutations(range(N+1)):
        if check_all(i):
            answer.append(i)
    print(answer, len(answer))
    return answer
    return [[0,1,2,3,4]]
    return answer

if __name__ == '__main__':
    import os
    os.system("python3 make_grid.py")

    
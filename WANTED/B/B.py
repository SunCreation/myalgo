""" B번 - 숫자 이어 붙이기
시간 제한	메모리 제한
1 초	512 MB
문제
철수는 수를 이어 붙이는 놀이를 좋아한다. 1과 2를 이어 붙이면 12가 되고, 17과 13을 이어 붙이면 1713이 된다. 100과 1000을 이어 붙이면 1001000이 된다. 1과 2를 이어 붙이되, 순서를 반대로 해서 2와 1을 이어 붙이면, 21이 된다. 같은 두 수를 이어 붙이더라도, 이어 붙이는 순서에 따라서 값이 달라진다는 것을 알 수 있다.

철수가 살고 있는 마을에는 집이 여러 채 있고, 각 집에는 $1$부터 $N$까지 번호가 붙어있다. 두 집 사이에 존재하는 도로를 통해 서로 이동할 수 있다. 총 $N-1$개의 도로가 존재한다. $i$번째 도로는 $a_i$번 집과 $b_i$집을 잇는다. 집과 도로는 트리의 형태를 이룬다. 즉, 어떤 집에서 시작해서 몇 개의 도로를 거쳐 어떤 집이라도 갈 수 있고, 같은 집을 두 번 방문하지 않을 경우 그 경로는 유일하다.

각각의 집의 대문에는 수가 쓰여있다. 철수는 총 $Q$번 수를 이어 붙이는 놀이를 할 것이다. $i$번째 놀이에서는 $x_i$번째 집에서 시작해서, $y_i$번째 집까지 이동하면서, 이동하는 경로 상에 있는 집들의 대문에 쓰여있는 수들을 방문하는 순서대로 이어 붙일 것이다. 만약 $x_i = y_i$라면, $x_i$번째 집의 대문에 쓰인 수가 답이 될 것이다. 철수는 놀이가 끝날 때마다, 자기가 올바르게 수들을 이어 붙였는지 궁금해졌다. 철수를 위해, $i$번째 놀이가 끝났을 때 이어 붙인 수의 값을 구해주자. 단, 수가 너무 커질 수 있으니까, $1\,000\,000\,007$로 나눈 나머지를 출력하도록 하자.

입력
첫 번째 줄에는 집의 개수 $N$과, 철수가 놀이를 할 횟수 $Q$가 주어진다.

두 번째 줄에는 $N$개의 집의 대문에 쓰여 있는 수 $A_i$가 공백을 사이에 두고 순서대로 주어진다.

세 번째 줄부터 $N+1$번째 줄까지는, 도로의 정보가 주어진다. $2+i$번째 줄에는 $i$번째 도로가 잇는 두 집의 번호 $a_i, b_i$에 대한 정보가 공백을 사이에 두고 주어진다.

 $N+2$번째 줄부터 $N+Q+1$번째 줄까지는 놀이에 대한 정보가 주어진다. $N+i+1$번째 줄에는 $i$번째 놀이를 시작할 집의 번호 $x_i$와, 끝낼 집의 번호 $y_i$가 공백을 사이에 두고 주어진다.

출력
첫 번째 줄부터 $Q$번째 줄에 걸쳐, $i$번째 줄에는 $i$번째 놀이의 결과를 $1\,000\,000\,007$로 나눈 나머지를 출력한다.

제한
 $2\leq N \leq 1\,000$ 
 $1\leq Q \leq 1\,000$ 
 $1 \leq A_i \leq 1\,000\,000\,000$ ($1 \leq i \leq N$)
 $1 \leq a_i, b_i \leq N$ 
 $1 \leq x_i, y_i \leq N$ 
예제 입력 1 
3 2
10 9 1
1 2
2 3
1 3
3 1
예제 출력 1 
1091
1910 """
# Q번 붙이기 놀이
# i번째 놀이에서 xi에서 yi집까지 이동하면서 대문에 쓰인 번호를 순서대로 붙임
# 1000000007로 나눔
from sys import stdin
from collections import deque


stdin = open('data','r')

N, Q = map(int,stdin.readline().split())

# 대문에 쓰인 숫자
Ai = stdin.readline().split()

homegraph = [[0]*(N+1) for _ in range(N+1)]
hometree = [0]*(N+1)

def myroot(home) -> list:
    global hometree
    homeroot = []
    while home:
        homeroot.append(home)
        home = hometree[home]
    return homeroot

for i in range(N-1):
    ai, bi = map(int, stdin.readline().split())
    homegraph[ai][bi]=1
    homegraph[bi][ai]=1

checkin = set()
stack = [1]
while stack:
    n = stack.pop()
    checkin.add(n)
    for i, j in enumerate(homegraph[n]):
        if not i in checkin and j:
            hometree[i] = n
            stack.append(i)
    
# N+2 부터 N+Q+1까지는 놀이에 대한 정보
for q in range(Q):
    xi, yi = map(int, stdin.readline().split())
    Xi, Yi = myroot(xi), myroot(yi)
    qXi = deque(Xi)
    root = set(Xi) & set(Yi)
    answer = ''
    while True:
        now = qXi.popleft()
        answer += Ai[now-1]
        if now in root:
            break
    while Yi:
        now = Yi.pop()
        if now in root:
            pass
        else:
            answer += Ai[now-1]
    print(int(answer)%1000000007)



# print(myroot(3), answer)
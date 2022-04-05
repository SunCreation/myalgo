""" 
문제
준겸이는 모험가이다. 모험을 떠나기 위해서는 철저한 사전 준비를 갖추어야 한다.
준겸이는 모험을 떠나기 전 $N$종류의 물약을 모두 구매하려고 한다. 물약 상점에 들른 준겸이는 각 물약이 $1$번부터 $N$번까지 번호가 매겨져 있다는 것을 알아냈다. 그런데, 물약 상점에서는 오늘 특별한 이벤트를 하고 있었다. 특정 물약을 구매하면, 어떤 다른 물약들을 할인해준다는 것이었다.
원래 $i$번째 물약의 가격은 동전 $c_i$개이다. 만약 $i$번째 물약을 구매하면, $p_i$종류의 다른 물약의 가격이 내려간다.
할인은 중첩된다. 예를 들어 $1$번 물약을 구매하면 $3$번 물약의 가격이 동전 $1$개만큼 할인되고, $2$번 물약을 구매하면 역시 $3$번 물약의 가격이 동전 $2$개만큼 할인된다고 하자. 그러면 두 물약을 모두 구매하고 나서 $3$번 물약을 구매할 때 동전 $3$개만큼의 할인을 받을 수 있다. 단, 물약의 가격이 내려가더라도 $0$ 이하로 내려가지는 않는다. 예를 들어, 원래 가격이 동전 $5$개인 물약이 동전 $4$개를 넘는 만큼 할인되더라도 가격은 동전 $1$개가 된다. 
준겸이는 신나서 물약을 구매하려다가, 물약을 구매하는 순서가 중요하다는 사실을 깨달았다. 준겸이를 위해 물약을 가장 싸게 샀을 때 그 비용을 알려주자.

입력
첫째 줄에 물약의 종류 $N$이 주어진다.

둘째 줄에 물약의 가격 $c_i$가 공백을 사이에 두고 주어진다($1 \le i \le N$). 

다음 줄부터, 물약 할인 정보가 $N$개 주어진다. $i$번째로 주어지는 물약 할인 정보는 다음과 같다($1 \le i \le N$). 

$p_i$가 주어진다. 다음 $p_i$개의 줄에, 물약 번호 $a_j$와 할인되는 가격 $d_j$가 주어진다. 이는 $i$번 물약을 구매하고 나면 물약 $a_j$가 동전 $d_j$개만큼 할인된다는 뜻이다.

출력
첫째 줄에 물약을 가장 싸게 샀을 때 동전이 몇 개 필요한지 출력한다. 

제한
 $2 \le N \le 10$ 
 $1 \le c_i \le 1\,000$ 
 $0 \le p_i \le N-1$ 
각 $i$에 대해, 모든 $a_j$는 서로 다르고 $a_j \neq i$ 
 $1 \le d_j \le 1\,000$ 
예제 입력 1 
4
10 15 20 25
2
3 10
2 20
0
1
4 10
1
1 10
예제 출력 1 
36
동전 10개를 지불하고 1번 물약을 구매하면, 3번 물약이 동전 10개만큼 할인되어 값이 동전 10개가 된다. 2번 물약은 동전 20개만큼 할인되어야 하지만, 최소 1개는 지불해야 하므로 값이 동전 1개가 된다. 그 후 동전 10개를 지불하고 3번 물약을 구매하면, 4번 물약이 동전 10개만큼 할인되어 값이 동전 15개가 된다. 그 후에 3번 물약과 4번 물약을 동전 1개와 10개를 내고 각각 구매하면 총 36개의 동전을 내고 모든 물약을 구매할 수 있다. """
from sys import stdin
from collections import defaultdict
from itertools import permutations

stdin = open('data', 'r')

N = int(stdin.readline())
ci = list(map(int,stdin.readline().strip().split())) # 물약 가격

# 할인정보
count_off = defaultdict(list)
# 할인 결과
answer = []
for i in range(N):
    pi = int(stdin.readline())
    for j in range(pi):
        count_off[i+1].append(stdin.readline().split())

for order in permutations(enumerate(ci),N):
    off_list = [0]*(N+1)
    t_price = 0
    for i,j in order:
        t_price += j - off_list[i+1]
        for k,m in count_off[i+1]:
            k = int(k)
            off_list[k] += int(m)
            if off_list[k] >= ci[k-1]:
                off_list[k] = ci[k-1] - 1
    answer.append(t_price)
    

# print(ci)
# print(count_off)
print(min(answer))
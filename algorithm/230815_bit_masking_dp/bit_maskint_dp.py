'''
비트마스킹을 활용한 동적 프로그래밍은 다양한 문제에 적용될 수 있습니다. 그 중 가장 대표적인 예로 **Traveling Salesman Problem (TSP)**를 들 수 있습니다.

TSP는 다음과 같은 문제입니다:

주어진 도시들 사이의 거리가 주어졌을 때, 시작 도시에서 출발해 모든 도시를 정확히 한 번씩 방문하고 다시 시작 도시로 돌아오는 가장 짧은 경로를 찾는 문제입니다.
'''

from pprint import pprint

n = int(input())  # 도시의 개수
INF = float('inf')
dist = [list(map(int, input().split())) for _ in range(n)]  # 각 도시 간의 거리
dp = [[INF] * (1 << n) for _ in range(n)]  # dp 테이블 초기화

# 시작점은 0번 도시로 가정
dp[0][1] = 0

for mask in range(1, 1 << n):
    '''
    u: 현재 고려하고 있는 도시입니다.
    v: 이전에 방문한 도시로, u 도시로 바로 이동하기 전에 마지막으로 방문한 도시입니다.
    '''
    for u in range(n):
        # 현재 상태에서 u 도시를 아직 방문하지 않았다면 체크할 필요가 없음
        print(u, bin(mask))
        '''
        mask & (1 << u) 연산은 mask의 u번째 비트가 1인지 아닌지를 확인하는 비트 연산입니다.

        1 << u: u번째 비트만 1이고 나머지 비트는 0인 숫자를 만듭니다.
        mask & (1 << u): mask와 위에서 생성한 숫자를 AND 연산하여 u번째 비트가 1인지 확인합니다.
        '''
        if not (mask & (1 << u)):
            # print(u, bin(mask), "안됨")
            continue
        for v in range(n):
            # v에서 u로 직접 갈 수 없거나, v를 이미 방문했으면 continue
            if not (mask & (1 << v)) or dist[v][u] == 0:
                continue
            # 현재 상태에서의 최소 비용을 갱신
            dp[u][mask] = min(dp[u][mask], dp[v][mask ^ (1 << u)] + dist[v][u])

ans = INF

pprint(dp)
for u in range(1, n):
    if dist[u][0] != 0:
        ans = min(ans, dp[u][(1 << n) - 1] + dist[u][0])

print(ans)

'''
Input
4
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0
Output
80
'''
'''
  0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111
[[inf, 0  , inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
 [inf, inf, inf, 10 , inf, inf, inf, 50 , inf, inf, inf, 45 , inf, inf, inf, 70],
 [inf, inf, inf, inf, inf, 15 , inf, 45 , inf, inf, inf, inf, inf, 50 , inf, 65],
 [inf, inf, inf, inf, inf, inf, inf, inf, inf, 20 , inf, 35 , inf, 45 , inf, 75]
'''
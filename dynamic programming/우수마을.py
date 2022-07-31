'''
인접의 인접이 내 자신일 수있음...!

'''


import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)


def dfs(V):
    global visited
    visited[V] = True
    if dp[V] != -1:
        return dp[V]
    # print(f'{V} 노드 탐색')

    adjSum = 0
    adjOfAdjSum = 0
    for adjV in E[V]:
        if visited[adjV]:
            continue
        # print(f'{V} 인접노드 계산: {adjV}')
        adjSum += dfs(adjV)
        for adjOfAdjV in E[adjV]:
            if adjOfAdjV == V:
                continue
            # print(f'{V} 인접의 인접노드 계산: {adjOfAdjV}')
            adjOfAdjSum += dfs(adjOfAdjV)
    dp[V] = max(adjSum, adjOfAdjSum + arr[V])
    # print(f'V:{V}, adj Sum:{adjSum}, adjOfAdj: {adjOfAdjSum}, dp[V]: {dp[V]}')
    return dp[V]


N = int(input())
arr = [0] + list(map(int, input().split()))
E = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)
init = 0
for i in range(1, N+1):
    if len(E[i]) == 1:
        init = i
        break

# print(init)
visited = [False for _ in range(N+1)]
dp = [-1 for _ in range(N+1)]
print(dfs(init))
# print(dp)

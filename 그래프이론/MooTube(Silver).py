import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)


def dfs(V, k):
    global answer
    visited[V] = True
    for u, r in E[V]:
        if visited[u] or r < k:
            continue
        answer += 1
        dfs(u, k)
    visited[V] = False


N, Q = map(int, input().split())


E = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v, r = map(int, input().split())
    E[u].append([v, r])
    E[v].append([u, r])

qArr = []
for _ in range(Q):
    qArr.append(list(map(int, input().split())))

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for k, v in qArr:
    visited = [False for _ in range(N+1)]
    answer = 0
    dfs(v, k)
    print(answer)

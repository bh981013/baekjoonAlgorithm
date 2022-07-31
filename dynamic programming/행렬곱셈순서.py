import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
dp = [[0 for _ in range(N)] for _ in range(N)]
for size in range(2, N+1):
    for startIdx in range(0, N-size+1):
        i, j = startIdx, startIdx+size-1
        dp[i][j] = min([dp[i][k] + dp[k+1][j] + arr[i][0] *
                       arr[k][1] * arr[j][1] for k in range(i, j)])
print(dp[0][N-1])

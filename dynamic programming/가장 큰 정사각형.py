import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
arr = []
dp = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    arr.append(input())

for j in range(0, M):
    dp[0][j] = int(arr[0][j])
for i in range(0, N):
    dp[i][0] = int(arr[i][0])

for i in range(1, N):
    for j in range(1, M):
        if arr[i][j] == "0":
            continue
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
# print("\n".join(map(str, dp)))
print(max(map(max, dp))**2)

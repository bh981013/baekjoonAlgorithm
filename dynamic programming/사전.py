import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)

N, M, K = map(int, input().split())
dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
for i in range(N+1):
    dp[0][i] = 1
for i in range(M+1):
    dp[i][0] = 1

for i in range(1, M+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
# print("\n".join(map(str, dp)))
length = N + M
output = []
if(dp[M][N] < K):
    print(-1)
    exit(0)
while(len(output) < length):
    if N == 0:
        output.append("z"*M)
        break
    elif M == 0:
        output.append("a" * N)
        break
    elif dp[M][N-1] < K:
        output.append("z")
        K -= dp[M][N-1]
        M -= 1
    else:
        output.append("a")
        N -= 1
    # print(output, f'K:{K}, N:{N}, M;{M}')
print("".join(output))

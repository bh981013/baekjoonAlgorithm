import sys
input = sys.stdin.readline
def main(): 
    TC = int(input())
    A = []
    for _ in range(TC):
        N = int(input())
        arr = list(map(int, input().split()))
        S = [arr[0]]
        dp = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(1,N-1):
            S.append(S[i-1] + arr[i])
        for i in range(1,N+1):
            for j in range(N):
                dp[j][i + j] = float("inf")
                for k in range(j, j+i):
                    dp[j][i + j] = min(dp[j][i + j], dp[j][k] + dp[k + 1][i + j] + S[i + j] - S[j - 1])
        print(dp[0][N-1])
main()
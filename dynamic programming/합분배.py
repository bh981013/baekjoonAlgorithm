'''
N-1, N-2... 0 을 만드는 모든 경우의 수 를 더함
'''

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
    for i in range(0, N+1):
        dp[1][i] = 1
    for i in range(0, K+1):
        dp[i][0] = 1
    for j in range(2, K+1):
        for i in range(1, N+1):
            dp[j][i] = dp[j-1][i] + dp[j][i-1]
    print(dp[K][N] % 1000000000)


main()

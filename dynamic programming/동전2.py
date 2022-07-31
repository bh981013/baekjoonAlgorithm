'''

'''
import sys
input = sys.stdin.readline
def main():
    n, k = map(int, input().split())
    coins = [0 for _ in range(n)]
    for i in range(n):
        coins[i] = int(input())
    dp = [-1 for _ in range(k+1)]
    dp[0] = 0
    for coin in coins:
        for i in range(k+1):
            if(i-coin<0):
                continue
            elif dp[i] == -1 and dp[i-coin] != -1:
                dp[i] = dp[i-coin] +1
            elif dp[i-coin] == -1 and dp[i] != -1:
                continue
            else:
                dp[i] = min(dp[i], dp[i-coin]+1)
    print(dp[k])

main()
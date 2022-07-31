'''
동전 가격의 오름차순으로 계산하는데,
특정 동전을 사용하지 않고 가격을 채우는 경우와 사용해서 채우는 경우 두가지로 계산

경우의 수 핵심
1. 전체 경우의 수를 따졌는가?
2. 중복해서 계산한 경우는 없는가?
'''
import sys
input = sys.stdin.readline
def main():
    n, k = map(int, input().split())
    coins = [0 for _ in range(n)]
    for i in range(n):
        coins[i] = int(input())
    dp = [0 for _ in range(k+1)]
    for i in range(n+1):
        dp[0] = 1
    for i in range(1,n+1):
        coin = coins[i-1]
        for j in range(k+1):
            if(j-coin<0):
                continue
            else:
                dp[j] = dp[j] + dp[j-coin]
    print(dp[k])

main()
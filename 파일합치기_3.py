'''
특정 구간의 최솟값을 구하는 함수를 만듬.
그 함수는 모든 분기점을 반복하며 재귀로 구함.
특정 구간의 최솟값을 이미 구했으면 또 구할필요 없음
----
재귀 사용할시 시간초과 극복 가능!!
'''

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)

# dp = [값, 비용여부]

TC = int(input())
for _ in range(TC):
    K = int(input())
    arr = list(map(int, input().split()))
    sumArr = [sum(arr[0:i+1]) for i in range(K)]

    dp = [[0 for _ in range(K)] for _ in range(K)]

    for cnt in range(K-1, 0, -1):
        for i in range(0, cnt):
            minCost = float("inf")
            j = i+K-cnt
            for k in range(i, j):
                minCost = min(dp[i][k] + dp[k+1][j] +
                              sumArr[j] - sumArr[i] + arr[i], minCost)
            dp[i][j] = minCost
    print(dp[0][K-1])

'''
dp[An번째 메모리까지 존재할 때][특정 비용 내에서] = 확보가능한 최대 메모리
'''

import bisect
import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
mems = list(map(int, input().split()))
costs = list(map(int, input().split()))
sumCost = sum(costs)
dp = [0 for _ in range(sumCost+1)]

for appNum in range(0, N):
    for costLimit in range(sumCost, -1, -1):
        if(costLimit-costs[appNum] >= 0):
            dp[costLimit] = max(
                dp[costLimit], dp[costLimit-costs[appNum]]+mems[appNum])
    # print(dp)
# print("\n".join(map(str, dp)))
print(bisect.bisect_left(dp, M))

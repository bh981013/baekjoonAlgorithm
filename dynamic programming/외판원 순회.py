'''
특정 노드를 방문 한 후 목표 노드인 0까지 도착하는데 걸리는 최솟값을 저장.

'''

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)


def getCost(curV, visited):
    if dp[curV][visited] != -1:
        # print(
        #     f'curV: {curV}, minCost: {dp[curV][visited]}, visited:{visited}, saved found')
        return dp[curV][visited]
    else:
        minCost = float("inf")
        # print(f'curV: {curV}, visited: {visited}')
        for adjV in range(N):
            if arr[curV][adjV] > 0 and (visited >> adjV) & 1 == 0:
                # print(f'visitedCalc: {visited | 1 << adjV}, adjV: {adjV}')
                minCost = min(
                    minCost, arr[curV][adjV] + getCost(adjV, visited | 1 << adjV))
        dp[curV][visited] = minCost
        # print(f'curV: {curV}, minCost: {minCost}, visited:{visited}')
        return minCost


N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
dp = [[-1 for _ in range(2 << N)] for _ in range(N)]
for i in range(N):
    if arr[i][0] > 0:
        dp[i][(1 << N)-1] = arr[i][0]
# print("\n".join(map(str, dp)))
print(getCost(0, 1))

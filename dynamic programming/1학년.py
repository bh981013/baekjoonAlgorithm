'''
1. 재귀
2. 반복문
'''

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)


def valid(target):
    if 0 <= target <= 20:
        return True
    else:
        return False


N = int(input())
arr = list(map(int, input().split()))
dp = [[0 for _ in range(21)] for _ in range(N)]
dp[0][arr[0]] = 1
for i in range(1, N):
    for target in range(21):
        if dp[i-1][target] > 0:
            targetAdd, targetSub = target+arr[i], target-arr[i]
            # print(f'targetAdd:{targetAdd}, targetSub:{targetSub}')
            for nextTarget in [targetAdd, targetSub]:
                if valid(nextTarget):
                    dp[i][nextTarget] += dp[i-1][target]
# print("\n".join(map(str, dp)))
print(dp[N-2][arr[-1]])

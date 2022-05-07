

from sys import setrecursionlimit

import sys
Money = []
cacheNo0 = []
cacheYes0 = []
sys.setrecursionlimit(10**7)
def solution(money):
    global Money, cacheNo0, cacheYes0
    answer = 0
    Money = money
    N = len(Money)
    cacheYes0, cacheNo0 = [-1 for _ in range(N)], [-1 for _ in range(N)]
    answer = max(dp(1, N-1, 1), Money[0] + dp(2, N-2, 0))
    return answer

def dp(start, end, No0):
    global cacheNo0, cacheYes0

    if(No0):
        if end == 1:
            return Money[1]
        if end <= 0:
            return 0
        if cacheNo0[end] != -1:
            return cacheNo0[end]
        else:
            cacheNo0[end] = max(dp(1, end-1, No0), Money[end] + dp(1, end-2, No0))
            return cacheNo0[end]
    else:
        if end == 2:
            return Money[2]
        if end == 1:
            return 0
        if cacheYes0[end] != -1:
            return cacheYes0[end]
        else:
            cacheYes0[end] = max(dp(1, end-1, No0), Money[end] + dp(1, end-2, No0))
            return cacheYes0[end]
print(solution([1,5,2,1]))
# print(cacheNo0)
# print(cacheYes0)

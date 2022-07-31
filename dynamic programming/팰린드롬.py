'''
i~j 까지 팰린드롬인지 여부는
i+1 ~j-1 까지 팰린드롬인지 확인하면 됨.
'''

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)

N = int(input())
arr = list(map(int, input().split()))
numQ = int(input())
Q = []
for _ in range(numQ):
    Q.append(list(map(int, input().split())))
dp = [[0 for _ in range(N)] for _ in range(N)]

# dp[i][i] 는 무조건 팰린드롬이다.
for i in range(N):
    dp[i][i] = 1

# dp[i][i+1]은 두수가 같으면 팰린드롬이다.
for i in range(N-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1

for size in range(3, N+1):
    for startIdx in range(0, N-size+1):
        i = startIdx
        j = startIdx+size-1
        if dp[i+1][j-1] and arr[i] == arr[j]:
            dp[startIdx][startIdx+size-1] = 1

# print("\n".join(map(str, dp)))
for start, end in Q:
    print(dp[start-1][end-1])

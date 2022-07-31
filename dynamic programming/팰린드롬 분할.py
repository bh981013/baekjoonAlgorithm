from audioop import reverse
import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)

arr = input().rstrip()
L = len(arr)

dp = [[False for _ in range(L)] for _ in range(L)]

for i in range(L):
    dp[i][i] = True
for i in range(L-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = True
for l in range(3, L+1):
    for i in range(L-l+1):
        j = i+l-1
        if arr[i] == arr[j] and dp[i+1][j-1]:
            dp[i][j] = True
# print("\n".join(map(str, dp)))

cntMinArr = [0 for _ in range(L+1)]
cntMinArr[L-1] = 1
for i in reversed(range(L-1)):
    minCnt = float("inf")
    for j in reversed(range(i, L)):
        if dp[i][j]:
            minCnt = min(minCnt, cntMinArr[j+1]+1)
    cntMinArr[i] = minCnt
# for i in range(L):
#     print(f'{arr[i]}:{cntMinArr[i]}', end=",")
# print()
print(cntMinArr[0])
# start = 0
# result = 0
# while(start < L):
#     for end in reversed(range(start, L)):
#         if dp[start][end]:
#             print(arr[start:end+1])

#             result += 1
#             start = end+1
#             break
# print(result)

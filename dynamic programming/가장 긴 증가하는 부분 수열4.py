import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)

N = int(input())
arr = list(map(int, input().split()))
dp = [[0, -1] for _ in range(N)]

dp[0] = [1, -1]
for i in range(1, N):
    longestNum, longestIdx = 0, -1
    for j in range(0, i):
        if(arr[j] < arr[i] and dp[j][0] > longestNum):
            longestNum, longestIdx = dp[j][0], j
    dp[i] = [longestNum+1, longestIdx]
longestIdx = 0
for i in range(N):
    if dp[i][0] > dp[longestIdx][0]:
        longestIdx = i
result = []
# print(f'longestIdx: {longestIdx}')
curIdx = longestIdx
while(curIdx != -1):
    result.append(arr[curIdx])
    curIdx = dp[curIdx][1]
print(dp[longestIdx][0])
print(" ".join(map(str, result[::-1])))

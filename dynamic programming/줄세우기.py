import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

dp = [0 for _ in range(N)]
dp[0] = 1
for i in range(1, N):
    maxNum = 0
    for j in range(i):
        if(arr[i] > arr[j]):
            maxNum = max(dp[j], maxNum)
    dp[i] = maxNum + 1
# print(dp)a
print(N - max(dp))

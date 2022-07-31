import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)

MAXW = 40000
N = int(input())
arr = list(map(int, input().split()))
numQ = int(input())
arrQ = list(map(int, input().split()))

dp = [0 for _ in range(MAXW+1)]
dp[arr[0]] = 1
for i in range(1, N):
    temp = [0 for _ in range(MAXW+1)]
    temp[arr[i]] = 1
    for j in range(MAXW):
        if dp[j] == 1:
            for k in [abs(j-arr[i]), j, abs(j+arr[i])]:
                if k > MAXW:
                    continue
                temp[k] = 1
    dp = temp

# print(dp[:20])
for q in arrQ:

    if q >= len(dp) or dp[q] == 0:
        print("N", end=" ")
    else:
        print("Y", end=" ")

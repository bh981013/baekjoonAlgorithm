import sys
from this import s
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)

arr = input().rstrip()
N = len(arr)
dp = [0 for _ in range(N)]
dp[0] = 1
if(arr[0] == '0'):
    print(0)
    exit(0)
for i in range(1, N):
    if(arr[i] == '0' and (arr[i-1] >= '3' or arr[i-1] == '0')):
        print(0)
        exit(0)
    if(10 <= int(arr[i-1] + arr[i]) <= 26):
        if(i == 1):
            if(arr[i] == '0'):
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1] + 1
        else:
            if(arr[i] == '0'):
                dp[i] = dp[i-2]
            else:
                dp[i] = dp[i-2] + dp[i-1]
    else:
        dp[i] = dp[i-1]
# print(dp)
print(dp[N-1] % 1000000)

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)

MAX = 1000000000
N = int(input())
# N = 10
# testS = 0
# for N in range(1, 41):
dp = [[[[0 for _ in range(10)] for _ in range(10)]
       for _ in range(10)] for _ in range(N)]
for i in range(1, 10):
    dp[0][i][i][i] = 1
for size in range(1, N):
    for num in range(10):
        for start in range(0, 10):
            for end in range(start, 10):
                add = 0
                if(num != 0):
                    add += dp[size-1][num-1][start][end]
                if(num != 9):
                    add += dp[size-1][num+1][start][end]
                if start <= num <= end:
                    dp[size][num][start][end] += add
                elif start-1 == num:
                    dp[size][num][start-1][end] += add
                elif end+1 == num:
                    dp[size][num][start][end+1] += add

S = 0
for i in range(10):
    S += (dp[N-1][i][0][9]) % MAX
print(S % MAX)
#     testS += S
# print(testS)

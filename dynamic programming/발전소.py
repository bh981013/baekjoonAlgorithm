import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)


def recur(onBit):
    if dp[onBit] != -1:
        return dp[onBit]
    for i in range(N):
        if 1 << i & onBit == 1:
            filteredBit = onBit & (((1 << N) - 1) & ~(1 << i))
            recur(filteredBit)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
power = input().rstrip()
powerBit = 0
for i in range(N):
    if power[i] == 'Y':
        powerBit = powerBit | (1 << i)
P = int(input())
dp = [-1 for _ in range(1 << N)]
dp[powerBit] = 0
# for onCnt in range(N):
# for checkBit in range(N):

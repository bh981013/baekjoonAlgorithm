'''
오름차순 정렬 후 지금까지 가장 연결 긴 전깃줄에 추가(증가하는 수열 문제와 비슷함)
'''

import sys
sys.setrecursionlimit(10*8)
input = sys.stdin.readline
# sys.stdin = open("input2.txt")


def main():
    N = int(input())
    lines = []
    for _ in range(N):
        lines.append(list(map(int, input().split())))
    lines.sort(key=lambda x: x[0])
    endpoints = list(map(lambda x: x[1], lines))
    dp = [0 for _ in range(N)]
    dp[0] = 1
    for i in range(1, N):
        maxNum = 0
        for j in range(0, i):
            if(endpoints[j] < endpoints[i]):
                maxNum = max(maxNum, dp[j])
        dp[i] = maxNum+1
    print(N - max(dp))


main()

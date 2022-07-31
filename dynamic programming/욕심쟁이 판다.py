'''
주변 칸보다 작은 칸에서 출발해서 dfs 로 탐색
만약 특정 칸에 도착했을 때 이미 기록된 값이 내가 기록중인 값보다 크다면 탐색을 멈춘다.
->시간초과
----
경로의 문제 같은 경우는 경로의 순서가 정해져있으므로, 부분문제를 찾을 수있다~! 예를들어 1-3-5-7 의 부분 경로는 3-5-7 같은 느낌.
주변을 봤을 때 내가 가장 크다면, 나한테 출발해서 갈수 있는 가장 큰 값은 1, 그 주변에 작은 값은 2...의 방식이다.
'''

import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)


def valid(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False


N = int(input())
DIR = [[0, 1], [1, 0], [-1, 0], [0, -1]]
dp = [[-1 for _ in range(N)] for _ in range(N)]
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

sortArr = []
for i in range(N):
    for j in range(N):
        sortArr.append([arr[i][j], [i, j]])
sortArr.sort(key=lambda x: -x[0])

for cnt, point in sortArr:
    x, y = point
    maxNum = 0
    for dx, dy in DIR:
        nx, ny = x+dx, y+dy
        if(valid(nx, ny) and dp[nx][ny] != -1 and arr[nx][ny] > cnt):
            maxNum = max(maxNum, dp[nx][ny])
        dp[x][y] = maxNum + 1

print(max(list(map(max, dp))))

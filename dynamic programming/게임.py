'''
dfs 로 방문, 방문하면서 이미 방문한 칸에 도착하면 무한번 움직일 수 있는것임,
상하좌우 값을 비교
--------------
문제: 방문을 확인할 때 다 방문했으면 다 방문했으니 flag를 꺼야되는데 안끄고 계속
방문표시를 해둠...!
'''
import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)


def valid(n, m):
    return (0 <= n < N and 0 <= m < M) and arr[n][m] != 'H'


def dfs(n, m):
    # print("point:", n, m)
    jump = int(arr[n][m])
    if dp[n][m][VISIT] == 1:
        print(-1)
        exit(0)
    if dp[n][m][0] != -1:
        return max(dp[n][m])
    dp[n][m][VISIT] = 1
    ret = 0
    for dir in range(4):
        dn = DIR[dir][0] * jump
        dm = DIR[dir][1] * jump
        if(valid(n+dn, m+dm)):
            moves = dfs(n+dn, m+dm)
            dp[n][m][dir] = moves+1
            ret = max(ret, moves+1)
        else:
            dp[n][m][dir] = 1
            ret = max(ret, 1)
    dp[n][m][VISIT] = -1
    return ret


U, R, D, L = 0, 1, 2, 3
DIR = [[-1, 0], [0, 1], [1, 0], [0, -1]]
VISIT = 4
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
dp = [[[-1 for _ in range(5)] for _ in range(M)] for _ in range(N)]
print(dfs(0, 0))

# print("\n".join(map(str, dp)))

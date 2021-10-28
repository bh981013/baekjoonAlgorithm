import sys
import copy
from collections import deque
import heapq
input = sys.stdin.readline

sys.setrecursionlimit(10**5)
# sys.stdout.write()
maxint = 10**4
def main():
    M, N = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(N)]
    prior = []
    heapq.heappush(prior, [0, [0,0]])
    dist = [[maxint for _ in range(M)] for _ in range(N)]
    dist[0][0] = 0
    dir = ((1,0),(0,1),(-1,0),(0,-1))
    while(prior):
        W, V = heapq.heappop(prior)
        y,x = V
        if W>dist[y][x]:
            continue
        for dy, dx in dir:
            ny, nx = y+dy, x+dx
            if 0<=ny<N and 0<=nx<M:
                isWall = int(arr[ny][nx])
                if dist[ny][nx]>W+isWall:
                    dist[ny][nx] = W+isWall
                    heapq.heappush(prior, [W+isWall, [ny, nx]])
    print(dist[N-1][M-1])
main()

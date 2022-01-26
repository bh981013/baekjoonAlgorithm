'''
각 지점을 지날때 검정이면 +1을 함. 하지만 만약 더 짧은 거리를 발견하면 갱신함.
like djikstra
'''

import sys
import heapq
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def next(h, w, N):
    dH = [1,0,-1,0]
    dW = [0,1,0,-1] #오른쪽부터 시계방향
    dir  = []
  
    for dh, dw in zip(dH, dW):
        if 0<= h+dh < N and 0<=w+dw < N:
            dir.append([h+dh, w+dw])
    return dir

def main():
    N = int(input())
    maxNum = 3000
    arr = []
    for _ in range(N):
        arr.append(list(map(lambda x: not x,map(int , list(input().strip())))))
    H = [(0, [0,0])]
    # visited =[[False for _ in range(N)] for _ in range(N)]
    dist = [[maxNum for _ in range(N)] for _ in range(N)]
    dist[0][0] = 0
    while(H):
        d, p = heapq.heappop(H)
        h = p[0]
        w = p[1]
        if d > dist[h][w]:
            continue
        # visited[h][w] = True
        for nd, nw in next(h,w, N):
            if dist[nd][nw] > d + arr[nd][nw]:
                dist[nd][nw] = d + arr[nd][nw]
                heapq.heappush(H, (dist[nd][nw], [nd, nw]))
    # print("\n".join(map(str,arr)))
    # print()
    # print("\n".join(map(str,dist)))
    print(dist[N-1][N-1])
main()
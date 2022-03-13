import sys
from collections import deque
sys.setrecursionlimit(10**8)

cache = []
maxF, curF, up, down =0,0,0,0
visited = []
def main():
    global cache, maxF, curF, up, down, visited
    maxF, curF, tarF, up, down = map(int, input().split())
    cache = [-1 for _ in range(maxF+1)]
    visited = [False for _ in range(maxF+1)]
    cache[curF] = 0
    visited[curF] = True
    bfs()
    if cache[tarF] == -1:
        print("use the stairs")
    else : print(cache[tarF])


def bfs():
    global cache, maxF, curF, up, down, visited
    q = deque([[curF, 0]])
    cache[curF] = 0
    while(q):
        pop, cnt = q.popleft()
        for move in (up, -down):
            if 0<pop+move<=maxF and cache[pop+move] == -1:
                cache[pop+move] = cnt+1
                q.append([pop+move, cnt+1])




main()
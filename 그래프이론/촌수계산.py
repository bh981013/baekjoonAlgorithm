import sys
from collections import deque
def main():
    N = int(input())
    U, V = map(int, input().split())
    numE = int(input())
    E = [[] for _ in range(N+1)]
    for _ in range(numE):
        u,v = map(int, input().split())
        E[u].append(v)
        E[v].append(u)
    q = deque([[U,0]])
    visited = [0 for _ in range(N+1)]
    visited[U] = 1
    while(q):
        popped, dist = q.popleft()
        if popped == V:
            print(dist)
            return
        for adjV in E[popped]:
            if not visited[adjV]:
                visited[adjV] =1
                q.append([adjV, dist+1])
    print(-1)

main()
    

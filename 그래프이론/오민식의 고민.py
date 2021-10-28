import sys
import copy
from collections import deque
import heapq
input = sys.stdin.readline

sys.setrecursionlimit(10**5)
minint = -10**13
numV, numE = 0,0
def main():
    numV, startV, endV, numE = map(int, input().split())
    E = [[]for _ in range(numV)]
    for _ in range(numE):
        u,v,w = map(int, input().split())
        E[u].append([v,-w])
    money = list(map(int, input().split()))
    for here in range(numV):
        for e in E[here]:
            e[1] += money[e[0]]
    dist = [minint for _ in range(numV)]
    dist[startV] = money[startV]
    forever = False
    cycle = []
    visited = [ False for _ in range(numV)]
    for i in range(numV):
        changed = False
        targetChanged = False
        for V in range(numV):
            for adjV, adjW in E[V]:
                if dist[V] != minint and dist[adjV]< dist[V]+adjW:
                    dist[adjV] = dist[V]+adjW
                    changed= True
                    if i == numV-1:
                        cycle.append(adjV)
        if not changed:
            break
    if dist[endV] == minint:
        print("gg")
        return
    q= deque()
    while(cycle):
        V = cycle.pop()
        if visited[V]:
            continue
        q.append(V)
        while(q):
            V = q.popleft()
            visited[V] = True
            for adjV, none in E[V]:
                if adjV == endV:
                    forever = True
                    print("Gee")
                    return
                if not visited[adjV]:
                    visited[adjV] = True
                    q.append(adjV)

        
    else:
        print(dist[endV])
        

main()

import sys
import copy
from collections import deque
import heapq
input = sys.stdin.readline

sys.setrecursionlimit(10**5)
# sys.stdout.write()
maxint = 10**6
E = []
def main():
    global E
    numV, numE, initV = map(int, input().split())
    dist = [maxint for _ in range(numV+1)]
    E = [[]for _ in range(numV+1)]
    for _ in range(numE):
        u,v,w = map(int,input().split())
        E[u].append([v,w])
    dji(dist, initV)
    for i in range(1, numV+1):
        if i == initV:
            continue
        tempD = [maxint for _ in range(numV+1)]
        dji(tempD, i)
        dist[i] += tempD[initV]
    print(max(dist[1:]))

def dji(dist, initV):
    pr = []
    heapq.heappush(pr, [0, initV])
    dist[initV] = 0
    while(pr):
        W,V = heapq.heappop(pr)
        if W>dist[V]:
            continue
        for adjV, adjW in E[V]:
            if adjW+W<dist[adjV]:
                dist[adjV] = adjW+W
                heapq.heappush(pr, [adjW+W, adjV])
main()

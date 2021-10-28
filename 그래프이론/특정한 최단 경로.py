import sys
import copy
from collections import deque
import heapq
import math
input = sys.stdin.readline
printf = sys.stdout.write
sys.setrecursionlimit(10**5+10)
N = 0
maxnum = 10**9
E = []
def main():
    global E
    numV, numE = map(int, input().split())
    E = [[] for _ in range(numV+1)]
    dist1 = [maxnum for _ in range(numV+1)]
    dist2 = [maxnum for _ in range(numV+1)]
    dist3 = [maxnum for _ in range(numV+1)]

    
    for _ in range(numE):
        u,v,w = map(int, input().split())
        E[u].append([v,w])
        E[v].append([u,w])
    mustu, mustv = map(int, input().split())

    dist1[1] = 0
    dist2[numV] = 0
    dist3[mustu] = 0

    func(dist1,[0, 1])
    func(dist2, [0, numV])
    func(dist3, [0,mustu])
    res = min(dist1[mustu] + dist2[mustv], dist1[mustv] + dist2[mustu]) + dist3[mustv]
    # print(dist1)
    # print(dist2)
    if res >=maxnum:
        print(-1)
    else:
        print (res)
def func(dist1, init):
    global E
    q = []
    heapq.heappush(q, init)
    while(q):
        W, V = heapq.heappop(q)
        if W>dist1[V]:
            continue
        for adjV, adjW in E[V]:
            if W+adjW<dist1[adjV]:
                dist1[adjV] = W+adjW
                heapq.heappush(q, [W+adjW, adjV])

        

    

        
        
                


main()

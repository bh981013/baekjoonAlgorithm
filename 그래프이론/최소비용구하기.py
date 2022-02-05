import sys
import heapq

input = sys.stdin.readline
def main():
    numV = int(input())
    numE = int(input())
    E = [[] for _ in range(numV+1)]
    for _ in range(numE):
        u,v,w = map(int, input().split())
        E[u].append([v,w])
    initV, endV = map(int, input().split())
    dist = [float("inf") for _ in range(numV+1)]
    dist[initV] = 0
    q = [[0, initV]]
    while(q):
        w, v = heapq.heappop(q)
        if(dist[v] < w):
            continue
        else:
            for adjV, adjW in E[v]:
                if dist[adjV] > adjW + w:
                    dist[adjV] = adjW+w
                    heapq.heappush(q,[adjW+w, adjV])
    print(dist[endV])

main()
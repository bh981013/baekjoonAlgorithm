import heapq
import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

MAX_DIST = (2*10**5)*(10**3)+1
numV = 0
E  = []
def main():
    global numV, E
    numV, numE = map(int, input().split())
    E = [[] for _ in range(numV+1)]
    for _ in range(numE):
        u,v,w = map(int, input().split())
        E[u].append([w, v])
        E[v].append([w,u])
    mustV1, mustV2 = map(int, input().split())
    dist1 = dji(1)
    dist2 = dji(numV)
    dist3 = dji(mustV1)
    ans = (min(dist1[mustV1] + dist2[mustV2], dist1[mustV2] + dist2[mustV1]) + dist3[mustV2])
    if ans >= MAX_DIST:
        print(-1)
    else:
        print(ans)

def dji(V):
    global numV, E
    dist = [MAX_DIST for _ in range(numV+1)]
    dist[V] = 0
    heap = [[0,V]]
    while(heap):
        w, v = heapq.heappop(heap)
        if dist[v] < w:
            continue
        else:
            for adjW, adjV in E[v]:
                if dist[adjV] > adjW + w:
                    dist[adjV] = adjW+w
                    heapq.heappush(heap, [adjW+w, adjV])
    return dist

main()
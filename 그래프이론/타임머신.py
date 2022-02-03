import sys
input = sys.stdin.readline
def main():
    numV, numE = map(int, input().split())
    E = [[] for _ in range(numV+1)]
    dist = [float("inf") for _ in range(numV+1)]
    dist[1] = 0
    for _ in range(numE):
        u,v,w =map(int, input().split())
        E[u].append([v,w])
    for _ in range(numV-1):
        for v in range(1, numV+1):
            for u, w in E[v]:
                if(dist[u] > dist[v] + w):
                    dist[u] = dist[v] + w
    for v in range(1, numV+1):
        for u, w in E[v]:
            if(dist[u] > dist[v] + w):
                print(-1)
                return
    for d in dist[2:]:
        if d == float("inf"):
            print(-1)
        else: print(d)
            
main()
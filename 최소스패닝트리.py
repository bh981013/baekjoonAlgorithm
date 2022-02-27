import sys
import heapq
input = sys.stdin.readline
def main():
    numV, numE = map(int, input().split())
    E = [[] for _ in range(numV+1)]
    pq =[]
    for _ in range(numE):
        u,v,w = map(int, input().split())
        E[u].append([w,v])
        E[v].append([w,u])
    for e in E[1]:
        heapq.heappush(pq,e)
    visited =[False for _ in range(numV+1)]
    visited[1] = True
    ans = 0
    while(pq):
        w, u = heapq.heappop(pq)
        if visited[u]:
            continue
        else:
            visited[u] = True
            ans += w
            for e in E[u]:
                heapq.heappush(pq, e)
    print(ans)

main()
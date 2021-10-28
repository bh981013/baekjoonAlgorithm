import sys
import copy
from collections import deque
import heapq
input = sys.stdin.readline

sys.setrecursionlimit(10**5)
# sys.stdout.write()
maxint = 10**11
numV, numE = 0,0
K = 0
E = []
def main():
    global numV, numE, E, money,K
    numV, numE, K = map(int,input().split())
    E = [[] for _ in range(numV+1)]
    for _ in range(numE):
        u,v,w = map(int, input().split())
        E[u].append([v, w])
        E[v].append([u, w])
    cache = dji(1)
    print(cache[numV][K])

def dji(initV):
    cache = [[maxint for _ in range(K+1)] for _ in range(numV+1)]
    cache[1] = [0 for _ in range(K+1)]
    q = []
    heapq.heappush(q, [0, initV, 0]) #거리, vertex
    while(q):
        W, V, used= heapq.heappop(q)
        # print(f"V:{V}, W:{W}, usedK: {used}")
        if cache[V][used] < W:
            continue
        for adjV, adjW in E[V]:
            # print(f"{adjV}까지 거리 {adjW}")
            if used<K and (cache[V][used] <cache[adjV][used+1]):
                # print(f"{used+1} 만큼 포장했더니 거리가 {cache[V][used]}임")
                for i in range(used+1, K+1):
                    if cache[adjV][i] <= cache[V][used]:
                        break
                    cache[adjV][i] = cache[V][used]
                heapq.heappush(q, [cache[adjV][used+1], adjV, used+1])
            if cache[V][used]+adjW < cache[adjV][used]:
                # print(f"{used} 만큼 포장했더니 거리가 {cache[V][used]+adjW}임")
                for i in range(used, K+1):
                    if cache[adjV][i] <= cache[V][used]+adjW:
                        break
                    cache[adjV][i] = cache[V][used]+adjW
                heapq.heappush(q, [cache[adjV][used], adjV, used])
            
        
            

                
                
    # print("\n".join(map(str,cache)))
    return cache
        
main()

import sys
import copy
from collections import deque
import heapq
import math
input = sys.stdin.readline
printf = sys.stdout.write
sys.setrecursionlimit(10**5+10)
N = 0
parent = []
rank = []
def main():
    global rank, parent
    N, numParty = map(int, input().split())
    parent = [i for i in range(N+1)]
    rank = [0 for _ in range(N+1)]

    truth = list(map(int, input().split())) #진실을 알고있는 사람
    for t in range(1,truth[0]):
        union(truth[t], truth[t+1])
    party  =[]
    for i in range(numParty):
        temp = (list(map(int, input().split())))
        party.append(temp[1:])
        for i in range(1,temp[0]):
            union(temp[i], temp[i+1])
    impos = 0
    if truth[0] != 0:
        impos = find(truth[1])
    output = 0
    for p in party:
        cannot = False
        for person in p:
            if find(person) == impos:
                cannot =True
                break
        if not cannot:
            output += 1
    print(output)

    
def find(a):
    global parent
    pa = parent[a]
    if pa == a:
        return a
    else:
        parent[a] = find(pa)
        return parent[a]

def union(a, b):
    global rank
    pa,pb = find(a), find(b)
    if pa == pb:
        return
    if rank[pb] >rank[pa]:
        pa, pb = pb, pa
    if rank[pa] == rank[pb]:
        rank[pa] += 1
    parent[pb] = pa
    

    

        
        
                


main()

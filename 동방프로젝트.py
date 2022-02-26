import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**8)
parent = []
rank = []
ans = 0
def find(u):
    global parent
    if parent[u] == u:
        return u
    else:
        parent[u] = find(parent[u])
        return parent[u]

def union(u,v):
    global parent, rank, ans
    u = find(u)
    v = find(v)
    if u == v: return
    if u > v:
        u, v = v, u
    ans -= 1
    parent[v] = u


def main():
    global parent, rank, ans
    N = int(input())
    M = int(input())
    ans = N
    parent = [i for i in range(N+1)]
    rank = [1 for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        a = find(a)
        # print("a:", a)
        while(True):
            b = find(b)
            # print("b:", b)
            if a != b:
                union(a, b)
            else: break
            b = b - 1
    print(ans)
main()
vimport sys
import heapq
from collections import deque
import copy
input = sys.stdin.readline
sys.setrecursionlimit(100000)
# sys.stdout.write()
tree = []
arr = []
N = 0
def main():
    global tree, arr, N
    N = int(input())
    arr = list(map(int, input().split()))
    sortedArr = sorted(arr)
    N2R = {}
    for i in range(1, N+1):
        N2R[sortedArr[i-1]] = i
    for i in range(N):
        arr[i] = N2R[arr[i]]
    tree = [0 for _ in range(N+1)]
    output = 0
    for i in range(N):
        output += getTree(N) - getTree(arr[i])
        setTree(arr[i], 1)
    # print(tree)
    print(output)

def setTree(a, d):
    global tree, N
    # print(a)
    while(a<=N):
        tree[a] += d
        a += a & -a

def getTree(a):
    global tree
    ret = 0
    while(a>0):
        ret += tree[a]
        a &= a - 1
    return ret
        

main()

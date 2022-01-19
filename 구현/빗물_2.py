#구간트리를 이용한 풀이->메모리초과

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
# sys.stdin = open("input.txt", "r")
arr = []
arr2 = []
tree = []
H,W,N =0,0,0
def calc(l, r):
    ret = 0
    h = min(arr[l], arr[r])
    for i in range(l ,r+1):
        remain = h - arr[i]
        if(remain > 0):
            ret += remain
    return ret

def calcLeft(r):
    if(r == 0):
        return 0
    ret = 0
    index = 0
    h = getMax(1,0,r-1,0,N-1)
    index = h[1]
    ret += calc(index,r)
    ret += calcLeft(index)
    return ret

def calcRight(l):
    if(l == N-1):
        return 0
    ret = 0
    maxH = 0
    index = N-1
    h = getMax(1,l+1,N-1,0,N-1)
    index = h[1]
    ret += calc(l, index)
    ret += calcRight(index)
    return ret

#노드가 표현하는 구간이 left:right임.
def initTree(node, left, right):
    global tree, arr, N
    if(left == right):
        tree[node] = arr2[left]
        return tree[node]
    L = initTree(node*2, left, (left+right) // 2)
    R = initTree(node*2+1, (left+right)//2+1, right)
    if(L[0] < R[0]):
        tree[node] = R
    else:
        tree[node] = L
    return tree[node]

def getMax(node, left, right, leftN, rightN):
    if rightN<left or right <leftN:
        return [0,-1]
    elif left <= leftN and rightN <= right:
        return tree[node]
    mid = (leftN+rightN) // 2
    L = getMax(node*2, left, right, leftN, mid)
    R = getMax(node*2+1, left, right, mid+1, rightN)
    ret = []
    if(L[0] < R[0]):
        ret = R
    else:
        ret = L
    return ret
        
def main():
    global H, W, arr, N, tree, arr2
    H,W = map(int, input().split())
    arr = list(map(int, input().split()))
    arr2 = []
    for i, a in enumerate(arr):
        arr2.append([a,i])
    N = len(arr)
    tree = [0 for _ in range(4*N)]
    ret = 0
    initTree(1,0, N-1)
    high= getMax(1, 0, N-1, 0,N-1)
    ret += calcLeft(high[1])
    ret += calcRight(high[1])
    print(ret)

main()
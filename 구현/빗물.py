#정답

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
# sys.stdin = open("input.txt", "r")

'''
최댓값을 중심으로 좌우로 다음을 큰값을 구한다음 물의 양계산. 반복

'''
arr = []
H, W = 0,0
N = 0
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
    maxH = 0
    index = 0
    for i in range(r):
        if(maxH < arr[i]):
             maxH = arr[i]
             index = i
    ret += calc(index,r)
    ret += calcLeft(index)
    return ret

def calcRight(l):
    if(l == N-1):
        return 0
    ret = 0
    maxH = 0
    index = N-1
    for i in range(N-1, l, -1):
        if(maxH < arr[i]):
             maxH = arr[i]
             index = i
    ret += calc(l, index)
    ret += calcRight(index)
    
    return ret


def main():
    global arr,H,W,N
    H, W = map(int, input().split())
    arr = list(map(int, input().split()))
    N = len(arr)
    highest = 0
    index = 0
    ret = 0
    for i in range(N):
        if(highest < arr[i]):
            highest =arr[i]
            index = i
    ret += calcLeft(index)
    ret += calcRight(index)
    print(ret)

main()

import sys
sys.setrecursionlimit(10**9)


RED = 0
GREEN = 1
BLUE = 2
cache,arr = [],[]

def main():
    global cache, arr
    N = int(input())
    arr = []
    cache = [[-1 for _ in range(3)] for _ in range(N)]
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    cache[0] = arr[0]
    print(min(getMax(RED, N-1), getMax(GREEN, N-1), getMax(BLUE, N-1)))

def getMax(color, ith):
    global cache, arr
    if cache[ith][color] != -1:
        return cache[ith][color]
    else:
        minNum = 10**7
        for c in range(3):
            if c == color:
                continue
            else:
                minNum = min(getMax(c, ith-1), minNum)
        cache[ith][color] = minNum + arr[ith][color]
        return cache[ith][color]

main()
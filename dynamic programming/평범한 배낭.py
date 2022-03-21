from re import S
import sys
input = sys.stdin.readline

cache = []
arr = []
def main():
    global cache,arr
    maxStuffNum, maxW = map(int, input().split())
    cache = [[0]+[-1 for _ in range(maxW)] for _ in range(maxStuffNum+1)]
    cache[0] = [0 for _ in range(maxW+1)]
    arr = [[]]
    for _ in range(maxStuffNum):
        arr.append(list(map(int, input().split())))
    print(dp(maxStuffNum, maxW))


def dp(stuffNum, W):
    global cache,arr
    if  W<0:
        return -float("inf")
    elif cache[stuffNum][W] != -1:
        return cache[stuffNum][W]
    
    else:
        ret = max(dp(stuffNum-1, W-arr[stuffNum][0]) + arr[stuffNum][1], dp(stuffNum-1, W))
        cache[stuffNum][W]  =ret
        return ret
    


main()
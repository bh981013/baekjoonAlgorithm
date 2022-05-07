import sys
input = sys.stdin.readline
# unbounded knapsack
cache = []
arr = []
def main():
    global cache,arr
    maxStuffNum, maxW = map(int, input().split())
    
    arr = [[]]
    finalStuffNum = 0
    for _ in range(maxStuffNum):
        v,c,k = list(map(int, input().split()))
        i = 1
        while(k > 0):
            arr.append([v*min(i,k),c*min(i,k)])
            k -= i
            i *= 2
            finalStuffNum += 1
    cache = [[0 for _ in range(maxW+1)] for _ in range(finalStuffNum+1)]
    cache[0] = [0 for _ in range(maxW+1)]
    for i in range(1, finalStuffNum+1):
        for j in range(1, maxW+1):
            if j - arr[i][0] < 0:
                cache[i][j] = cache[i-1][j]
            else:
                cache[i][j] = max(cache[i-1][j-arr[i][0]] + arr[i][1], cache[i-1][j])

    print(cache[finalStuffNum][maxW])


main()


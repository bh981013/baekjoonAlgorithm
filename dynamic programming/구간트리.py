
cache = []
def main():
    global cache
    num, secNum = map(int, input().split())
    cache = [[-1 for _ in range(101)] for _ in range(101)]
    arr = [0]
    for _ in range(num):
        arr.append(int(input()))
    result = [[0 for _ in range(num+1)] for _ in range(secNum+1)]
    for curSec in range(1, secNum+1):
        for i in range(1, num+1):
            M = 0
            for j in range(1, i-1):
                M = max(M, result[curSec-1][j]+getSum(j+2,i, arr))
            result[curSec][i] = M
    print(result)
    print(result[secNum][num])

def getSum(s,e, arr):
    global cache
    if cache[s][e] != -1:
        return cache[s][e]
    S = 0
    for i in range(s, e+1):
        S += arr[i]
    cache[s][e] = S
    return S

main()
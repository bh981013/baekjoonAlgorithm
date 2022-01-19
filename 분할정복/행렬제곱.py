import sys
import math
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10**9)
C = 1000


def sqr(arr1, arr2):
    N = len(arr1)
    ret = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            s = 0
            for k in range(N):
                 s += arr1[i][k] * arr2[k][j]
            ret[i][j] = s % C
    return ret



def main():
    N, B = map(int, input().split())
    arr = []
    ret = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    for i in range(N):
        ret[i][i] = 1
    while(B):
        mulCnt = int(math.log2(B))
        temp = arr
        for i in range(mulCnt):
            temp = sqr(temp, temp)
        ret = sqr(ret, temp)
        B = B - (2**mulCnt)
    for i in range(N):
        for j in range(N):
            print(ret[i][j], end = " ")
        print()
main()
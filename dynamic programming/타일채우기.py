import sys
input = sys.stdin.readline
indiv = []
getSum = []


def main():
    global indiv, getSum
    N = int(input())
    indiv = [2 for _ in range(N+2)]
    getSum = [-1 for _ in range(N+2)]
    indiv[2] = 3
    getSum[0] = 1
    getSum[2] = 3
    print(cnt(N))

def cnt(n):
    global getSum, indiv
    if getSum[n] != -1:
        return getSum[n]
    else:
        ret = 0
        for i in range(2, n+1, 2):
            ret += cnt(n-i) * indiv[i]
        getSum[n] = ret
        return ret

main()


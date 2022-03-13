import sys
# input = sys.stdin.readline
sys.stdin = open("input.txt", "r")
cache, arr, S = [],[], []
def main():
    global cache, arr, S
    TC = int(input())
    A = []
    for _ in range(TC):
        N = int(input())
        arr = list(map(int, input().split()))
        cache = [[-1 for _ in range(N)] for _ in range(N)]
        S = [[-1 for _ in range(N)] for _ in range(N)]
        dp(0, len(arr)-1)
        sys.stdout.write(str(S[0][N-1]) + "\n")

    

def dp(a, b):
    global cache, arr, S
    if cache[a][b] != -1:
        return cache[a][b]
    if a == b:
        cache[a][b] = arr[a]
        S[a][b] = cache[a][b]
        return cache[a][b]
    elif a == b-1:
        cache[a][b] = arr[a]+arr[b]
        S[a][b] = cache[a][b]
        return cache[a][b]
    else:
        answer = float("inf")
        for i in range(a, b):
            l = dp(a, i)
            r = dp(i+1, b)
            temp = 0
            if a == i:
                temp = S[i+1][b]
            elif b == i+1:
                temp = S[a][i]
            else: temp = S[a][i] + S[i+1][b]
            if answer> l+r+temp:
                answer= l+r+temp
        cache[a][b] = l+r
        S[a][b] = answer
        return cache[a][b]
    
main()
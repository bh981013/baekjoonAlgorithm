import sys
myInput = sys.stdin.readline
sys.setrecursionlimit(1000000)
N0,N1 = [],[]
cache = []
arr = []
def main():
    global N0, N1, cache, arr
    N = int(myInput())
    for i in range(N):
        arr.append(int(myInput()))
    cache = [[-1,-1] for _ in range(max(arr)+1)]
    cache[0] = [1,0]
    cache[1] = [0,1]
    for i in range(N):
        fib(arr[i], i)
        print(cache[arr[i]][0], cache[arr[i]][1])
def fib(n, i):
    global cache
    if cache[n] != [-1,-1]:
        return cache[n]
    else: 
        cache[n] = add(fib(n-1, i),fib(n-2, i))
        return cache[n]

def add(a,b):
    return [a[0]+b[0], a[1]+b[1]]
main()
            


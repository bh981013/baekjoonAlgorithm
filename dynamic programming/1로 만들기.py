from functools import cache
import sys
myInput = sys.stdin.readline
sys.setrecursionlimit(1000000)
N, output = 0,0
cache = []
def main():
    global N, output, cache
    N = int(myInput())
    cache = [0 for _ in range(max(4,N)+1)]
    cache[1], cache[2], cache[3] = 0,1,1
    find(N)
    print(cache[N])

def find(n):
    global cache, N, output
    for i in range(4,N+1):
        if(i%6==0):
            cache[i] = min(cache[i//2], cache[i//3], cache[i-1])+1
        elif(i%3==0):
            cache[i] = min(cache[i//3], cache[i-1])+1
        elif(i%2==0):
            cache[i] = min(cache[i//2], cache[i-1])+1
        else:
            cache[i] = cache[i-1] + 1
main()
            


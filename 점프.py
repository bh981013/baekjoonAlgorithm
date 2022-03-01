import sys

myInput = sys.stdin.readline
sys.setrecursionlimit(1000000)
output = 0
cache = []
arr = []
N = 0

def main():
    global output, cache, N, arr
    
    N = int(myInput())
    cache = [[-1 for _ in range(N)] for _ in range(N)]
    for _ in range(N):
        arr.append(list(map(int, myInput().split())))
    findPath(0,0)
    # for i in range(N):
    #     for j in range(N):
    #         print(cache[i][j], end = " ")
    #     print()
    print(output)
    
def findPath(y,x):
    global N, output, cache, arr
    if(y==N-1 and x == N-1):
        output += 1
        return 1
    if(y>=N or x>= N or arr[y][x] == 0):
        return 0
    ret = cache[y][x]
    if(ret != -1):
        output += ret
        return ret
    else: 
        jump = arr[y][x]
        temp1 = findPath(y+jump, x) 
        temp2 =  findPath(y, x+jump)
        ret = temp1 + temp2
        cache[y][x] = ret
        return ret


main()
            


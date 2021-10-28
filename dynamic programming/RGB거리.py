import sys
import copy
myInput = sys.stdin.readline
sys.setrecursionlimit(1000000)
arr = [[0,0,0]]
price = []
N = 0
def main():
    global arr, price, N
    N = int(myInput())
    for i in range(N):
        arr.append(list(map(int, myInput().split())))
    price = [[0,0,0] for _ in range(N+1)]
    price[1] = copy.copy(arr[1])
    find()
    print(min(price[N]))

def find():
    global arr, price, N
    C = [0,1,2]
    for n in range(2,N+1):
        for i in C:
            price[n][i] = arr[n][i] + min(price[n-1][(i+1)%3], price[n-1][(i+2)%3])
    
main()
            


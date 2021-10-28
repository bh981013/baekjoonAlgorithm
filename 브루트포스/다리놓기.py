import sys
import math
myInput = sys.stdin.readline
output = []

def main():
    N = int(myInput())
    arr = []
    result = []
    for i in range(N):
        arr.append(list(map(int, myInput().split())))
    for a, b in arr:
        result.append(C(a,b))
    print("\n".join(map(str,result)))

def C(a,b):
    return math.factorial(b)//(math.factorial(a)*math.factorial(b-a))




main()
        

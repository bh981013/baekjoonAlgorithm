import sys

myInput = sys.stdin.readline

def main():
    a,b = map(int,myInput().split())
    arr = [[0 for _ in range(b)] for _ in range(a)]
    for i in range(a):
        temp = myInput()
        for j in range(b):
            arr[i][j] = temp[j]
    S, B= min(a,b), max(a,b)
    for n in reversed(range(2,S+1)):
       for i in range(a-n+1):
           for j in range(b-n+1):
               x = arr[i][j] 
               if(x == arr[i+n-1][j] and x == arr[i][j+n-1] and x == arr[i+n-1][j+n-1]):
                   print(n**2)
                   exit(0)
    print(1)

main()                   

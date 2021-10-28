import sys
myInput = sys.stdin.readline
output = []

def main():
    N = int(myInput())
    count = 0
    for n in range(1, N+1):
        if(n>= 1 and n<100):
            count += 1
        elif(n>=100 and n<1000):
            three = n//100
            two = n %100 //10
            one = n % 10
            if three + one == 2*two:
                count+= 1
    print(count)

main()
        

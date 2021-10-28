import sys
import copy
myInput = sys.stdin.readline
count = 0
numbers = []
numOfNumbers,targetNum = 0,0
def main():
    global count, numOfNumbers, targetNum, numbers
    numOfNumbers, targetNum = map(int, myInput().split())
    numbers = list(map(int,myInput().split()))
    for i in range(1, numOfNumbers+1):
        add(0, i,-1)
    print(count)
   

def add(sum, remained, pickedIndex):
    global count, numOfNumbers, targetNum, numbers
    if remained == 0:
        if sum == targetNum: count+=1
        return
    for i in range(pickedIndex+1, numOfNumbers):
        sum+= numbers[i]
        add(sum, remained-1, i)
        sum-= numbers[i]
    


main()
        

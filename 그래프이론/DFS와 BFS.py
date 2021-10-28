import sys
from collections import deque

myInput = sys.stdin.readline

def main():
    V,E,initV = map(int,myInput().split())
    arr = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    myStack = [initV]
    myQueue = deque([initV])
    output1 = []
    output2 = []
    for _ in range(E):
        a,b = map(int,myInput().split())
        arr[a][b], arr[b][a] = 1,1
    

    while myStack:
        popped = myStack.pop()
        if visited[popped] == 0:
            output1.append(popped)
            for adj in reversed(range(1, V+1)):
                if visited[adj] == 0 and arr[popped][adj] == 1:
                    myStack.append(adj)
            visited[popped] = 1                
    

    visited = [0 for _ in range(V+1)]

    while myQueue:
        popped = myQueue.pop()
        if visited[popped] == 0:
            output2.append(popped)
            for adj in (range(1,V+1)):
                if visited[adj] == 0 and arr[popped][adj] == 1:
                    myQueue.appendleft(adj)
            visited[popped] = 1
            

    print(" ".join(map(str, output1)))
    print(" ".join(map(str, output2)))
main()

'''
만약 큐에 있는 시간이 length만큼 되면 popLeft한다.
pop되는순간 다음 트럭이 들어올수 있는지 확인한다.
-----------다른풀이---------
큐를 돈다
'''
import sys
from collections import deque
input = sys.stdin.readline

def main():
    numOfTruck, length, maxW = map(int, input().split())
    arr = deque(list(map(int, input().split())))
    remain = numOfTruck
    t = 0
    q = deque([0 for _ in range(length)])
    w = 0
    while(remain):
        t+=1
        doneTruck=  q.popleft()
        w -= doneTruck
        if doneTruck > 0:
            remain -= 1
        if arr and w + arr[0] <= maxW:
            nextTruck = arr.popleft()
            q.append(nextTruck)
            w += nextTruck
        else: q.append(0)
    print(t)    
main()
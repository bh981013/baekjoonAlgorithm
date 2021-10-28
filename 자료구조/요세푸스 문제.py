import sys
import heapq
from types import new_class
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

class person:
    def __init__(self, num):
        self.num = num
        self.next = next
    

def main():
    N,K = map(int,input().split())
    p = person(N)
    last = p
    temp = p
    arr = []
    for i in reversed(range(1, N)):
        bef = person(i)
        if i == N-1 and N >= 2:
            temp = bef
        bef.next = p
        p = bef
    last.next = p
    cur = last
    bef = temp
    for _ in range(N):
        jump = 0
        while(jump < K):
            bef = cur
            cur = cur.next
            jump+=1
        bef.next = cur.next
        arr.append(cur.num)
    a = ", ".join(list(map(str,arr)))
    print("<", end="")
    print(a, end="")
    print(">", end="")


                    





main()
            


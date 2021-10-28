from collections import deque
import sys
myinput = sys.stdin.readline
sys.setrecursionlimit(1000000)

L  =0
class node:
    def __init__(self, name):
        self.name = name
        self.next = []
        self.visited = False
        
def main():
    global L
    n = int(myinput())
    arr = [0]+[node(i) for i in range(1,n+1)]
    for _ in range(n):
        a,*b = map(int, myinput().split())
        for i in range(len(b)//2):
            arr[a].next.append([b[2*i],b[2*i+1]])
    getLarge(arr, 1)
    print(L)

def getLarge(arr, root):
    global L
    h = 0
    L1 = 0
    L2 = 0
    arr[root].visited = True
    for i in arr[root].next:
        if arr[i[0]].visited == False:
            t = getLarge(arr, i[0])+i[1]
            if L1<t:
                L2 = L1
                L1 = t
            elif t<=L1 and t>L2:
                L2 = t
            # print(t+i[1])
            # print(L1,L2)
    h = L1
    # print(f"{root}일때 최종 {L1}, {L2}")
    # if L<L1+L2:
    #     print(f"{root} 일때 {L}보다 {L1+L2}가 더크다")
    L = max(L, L1+L2)

    # print(str(arr[root].name)+"일때" +str(h))

    return h


main()


import sys
import copy
from collections import deque
import heapq
import math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
printf = sys.stdout.write
def topost(a1,b1, a2,b2):
    # print(a1,b1,a2,b2)
    if a1==b1:
        print(pre[a1])
        return
    if a1>b1 or b1>=len(pre):
        return
    for i in range(a2, b2+1):
        if inorder[i] == pre[a1]:
            break
    leftlen = i-a2
    topost(a1+1,a1+leftlen, a2, i-1)
    topost(a1+1+leftlen, b1, i+1, b2)
    print(pre[a1])
    return



pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break
inorder = sorted(pre)
topost(0, len(pre)-1, 0, len(inorder)-1)
        

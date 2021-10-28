import sys
import heapq
myinput = sys.stdin.readline
# sys.setrecursionlimit(1000000)
import time
import re
start = 0
def main():
    T =  int(input())
    signals = []
    output = []
    for _ in range(T):
        signals.append(input().strip())
    p = re.compile("(100+1+|01)+")
    for signal in signals:
        m = p.fullmatch(signal)
        if m!= None and m.span() == (0, len(signal)):
            output.append("YES")
        else: output.append("NO")
        
    print("\n".join(output))



    
main()

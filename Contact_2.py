import sys
input = sys.stdin.readline
END = -1
def main():
    state = 0
    N = int(input())
    S = []
    for _ in range(N):
        S.append(reversed(list(input().strip())))
    for s in S:
        while(state != END and s):
            p = s.pop()
            if state == 0:
                if p == 1:
                    state = 1
                else: state = -2
            elif state == 1:
                if p == 0:
                    state = 2
                else: state = -2
            elif state == 2:
                if p == 0:
                    state = 3
                else: state = -1
            elif state == 3:
                if p == 1:
                    state = 4
            elif state == 4:
                
                    
    
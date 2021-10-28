import sys
Input = sys.stdin.readline
output = 0
def main():
    global output
    N, r, c = map(int, Input().split())
    calculate(N,r,c)
    print(output)

def calculate(N,r,c):
    global output
    if(N==0):
        return
    #r과 c를 각각 2**(N-1)로 나눠서 몫만큼 특정값을 더하고 나머지를 따로 계산
    output += (2**(2*N-1)) * (r //2**(N-1)) + (2**(2*N-2)) * (c // 2**(N-1))
    calculate(N-1,r %(2**(N-1)), c%(2**(N-1)))

main()
    

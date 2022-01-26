import sys
sys.setrecursionlimit(10**5)

input =sys.stdin.readline
# sys.stdin = open("input.txt", "r")
N = 0
row, col, rd, ru = [[] for _ in range(4)]
output = 0

def getDiag(r, c):
    d = r+c
    u = ((N-1) + 2*c)-d
    return [d,u]

def calc(r, remain):    #point 부터 확인
    global output,row, col, rd, ru
    if remain == 0: 
        output+=1 
        return
    elif r>= N: return
    for c in range(0, N):
        # print("r",r, 'c', c,"remain",remain)
        if(col[c]):
            d, u = getDiag(r, c)
            if(rd[d] and ru[u]):
                # row[r] = False
                col[c] = False
                rd[d] = False
                ru[u] = False
                calc((r+1),remain-1)
                # row[r] = True
                col[c] = True
                rd[d] = True
                ru[u] = True

def main():
    global N, row, col, rd, ru, output
    N = int(input())
    # row = [True for _ in range(N)]
    col = [True for _ in range(N)]
    rd = [True for _ in range(2*N-1)]
    ru = [True for _ in range(2*N-1)]
    calc(0,N)
    print(output)
main()
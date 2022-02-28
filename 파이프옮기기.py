import sys
input = sys.stdin.readline

def main():
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    r, d, h = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
    r[0][1] = 1
    for y in range(N):
        for x in range(N):
            if arr[y][x] != 1:
                if x>=1:
                    r[y][x] += r[y][x-1] + h[y][x-1]
                if y>=1:
                    d[y][x] += d[y-1][x] + h[y-1][x]
            if x>=1 and y>=1 and arr[y][x] != 1 and arr[y-1][x] != 1 and arr[y][x-1]!= 1:
                h[y][x] += r[y-1][x-1] + d[y-1][x-1] + h[y-1][x-1]
    print(h[N-1][N-1] + r[N-1][N-1] + d[N-1][N-1])
    # print(h)
    # print(d)
    # print(r)
main()
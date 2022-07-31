import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)

L, D, R = 0, 1, 2
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

costArr = [[[0, 0, 0] for _ in range(M)] for _ in range(N)]
for i in range(3):
    costArr[-1][-1][i] = arr[-1][-1]
for i in reversed(range(M-1)):
    for j in range(3):
        costArr[-1][i][j] = costArr[-1][i+1][j] + arr[-1][i]


for i in reversed(range(N-1)):
    costArr[i][0][L] = -float("inf")
    costArr[i][M-1][R] = -float("inf")
    for j in range(M):
        if j > 0:
            costArr[i][j][L] = max(
                costArr[i][j-1][L], costArr[i][j-1][D]) + arr[i][j]
        costArr[i][j][D] = max(costArr[i+1][j])+arr[i][j]
    for j in reversed(range(M)):
        if j < M-1:
            costArr[i][j][R] = max(
                costArr[i][j+1][R], costArr[i][j+1][D]) + arr[i][j]

# print("\n".join(map(str, costArr)))
print(max(costArr[0][0]))

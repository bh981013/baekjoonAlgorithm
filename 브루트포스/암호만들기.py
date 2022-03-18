import sys

L, C = 0,0
t = 0
D = {}
def main():
    global L, C, arr, D
    L,C = map(int, input().split())
    arr= sorted(input().split())
    for alph in ["a", "i", "e", "u", "o"]:
        D[alph] = True
    recur("", -1,0,0)
def recur(temp, pickedIndex, numV, numC):
    global L, C, arr, D
    if len(temp) == L and numV >= 1 and numC >= 2:
        print("".join(temp))
    else:
        for i in range(pickedIndex+1, C):
            isV, isC = 0,0
            if D.get(arr[i]):
                isV = 1
            else:
                isC = 1
            recur(temp + arr[i], i, numV + isV, numC + isC)

main()
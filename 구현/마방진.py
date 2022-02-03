import sys
input = sys.stdin.readline
#sys.stdin = open("input.txt", "r")

RIGHT_DOWN = 0
RIGHT_UP = 1
P = []
DIR = []

def main():
    global P, DIR
    init()

    arr = []
    for _ in range(3):
        arr.append(list(map(int, input().split())))
    if arr[0][0] == arr[1][1] == arr[2][2] == 0 or arr[2][0] == arr[1][1] == arr[0][2] == 0:
        d = 0
        mode = -1
        if arr[0][0] == 0:
            d = arr[0][1] - arr[1][2]
            mode = RIGHT_DOWN
        else:
            d = arr[0][1] - arr[1][0]
            mode = RIGHT_UP
        partS = arr[0][1] + arr[2][1]
        x = (partS + d)//2
        if mode == RIGHT_DOWN:
            arr[0][0] = x - d
            arr[2][2] = x
        else:
            arr[0][2] = x-d
            arr[2][0] = x
        S = sum(arr[0])
        arr[1][1] = S - partS
    else:
        S = getSum(arr)
        check(S,arr)
    for i in range(3):
        print(" ".join(map(str,arr[i])))

def init():
    global P, DIR
    for i in range(3):
        for j in range(3):
            P.append([i,j])
    
    for i in range(3):  #ROW
        temp = []   
        for j in range(3):
            temp.append(P[3*i+j])
        DIR.append(temp)

    for i in range(3):  #COLUMN
        temp = []
        for j in range(3):
            temp.append(P[i+3*j])
        DIR.append(temp)

    temp = []   #RIGHT_DOWN
    for j in range(3):
        temp.append(P[4*j])
    DIR.append(temp)

    temp = []
    for j in range(1,4):
        temp.append(P[2*j])
    DIR.append(temp)

    

def check(S, arr):
    for _ in range(8):
        for dir in DIR:
            p1, p2, p3 = dir
            if  (arr[p1[0]][p1[1]] == 0 and arr[p2[0]][p2[1]] != 0 and arr[p3[0]][p3[1]] != 0):
                arr[p1[0]][p1[1]] = S - arr[p2[0]][p2[1]] - arr[p3[0]][p3[1]]
            elif  (arr[p1[0]][p1[1]] != 0 and arr[p2[0]][p2[1]] == 0 and arr[p3[0]][p3[1]] != 0):
                arr[p2[0]][p2[1]] = S - arr[p1[0]][p1[1]] - arr[p3[0]][p3[1]]
            elif  (arr[p1[0]][p1[1]] != 0 and arr[p2[0]][p2[1]] != 0 and arr[p3[0]][p3[1]] == 0):
                arr[p3[0]][p3[1]] = S - arr[p2[0]][p2[1]] - arr[p1[0]][p1[1]]
                


def getSum(arr):
    S = 0
    R = [True for _ in range(3)]
    C = [True for _ in range(3)]
    X = [True for _ in range(2)]
    for i in range(3):
        for j in range(3):
            if arr[i][j] == 0:
                R[i] = False
                C[j] = False
                if i == j:
                    X[RIGHT_DOWN] = False
                elif i+j == 2:
                    X[RIGHT_UP] = False
    for i in range(3):
        if R[i] == True:
            S = sum(arr[i])
            return S
        elif C[i] == True:
            S = arr[0][i] + arr[1][i] + arr[2][i]
            return S
        elif i<2 and X[i] == True:
            if i ==RIGHT_DOWN:
                S = arr[0][0] + arr[1][1] + arr[2][2]
            else:
                S = arr[2][0] + arr[1][1] + arr[0][2]
            return S

main()
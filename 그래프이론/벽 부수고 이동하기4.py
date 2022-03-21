'''
빈칸에서 출발해 인접한 벽들을 표시하고, 빈 칸 수를 셈.
빈칸 수를 다세면 인접한 벽들에 빈칸 수를 더함.

'''


from re import S
import sys
#input = sys.stdin.readline
sys.stdin = open("input.txt", "r")
print = sys.stdout.write
dirH = [0, 1, 0 ,-1]
dirW = [1,0,-1, 0]  #오른쪽, 아래, 왼쪽, 위
N, M =0,0

visited =  []
arr =[]
blank = []
adjWall, blankSize = [],[]
def main():
    global visited, arr, blank, N, M, adjWall, blankSize
    N, M = map(int, input().split())
    MAP_SIZE = N*M
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().strip())))
    #print(arr)
    #map을 돌면서 빈칸을 확인함.
    adjWall = []
    blankSize = []
    visited = [[0 for _ in range(M)] for _ in range(N)]
    cur = 0
    while(cur < MAP_SIZE):
        h = cur // M
        w = cur % M
        #print(h, w)
        if visited[h][w] or arr[h][w] > 0:  #이미 방문한 빈칸이거나, 벽일땐 무시하고 다음 칸을 확인.
            #print("this is wall or visited")
            cur += 1
        else:   #방문하지 않은 빈칸 발견
            #print("this is blank")
            dfs(h,w)   # h,w 에서 시작하고 blankNum번째 빈칸묶음
            cur += 1
    for i in range(len(adjWall)):
        for h, w in adjWall[i]:
            arr[h][w] += blankSize[i]
    #print()
    for i in range(N):
        print("".join(map(str,(map(lambda x: x % 10, arr[i])))))
        print("\n")
    #print("\n".join(map(str, blankSize)))
    #print(blankSize)
    #print("\n".join(map(str,adjWall)))

def dfs(h,w):
    global visited, arr, blank, adjWall, blankSize,N, M
    stack = [[h,w]]
    visited[h][w] = 1
    walls = []
    sizeOfBlank = 1
    visitedWall = [[0 for _ in range(M)] for _ in range(N)]
    #dfs 로 빈칸을 탐색하면서 벽을 만났을때, 빈칸을 만났을 때 다른 작업을 수행
    while(stack):
        #print(stack)
        h,w = stack.pop()
        #print("new:", h, w)
        for dh, dw in zip(dirH, dirW):
            nh,nw = h+dh, w+dw
            #print(nh, nw)
            if 0<=nh<N and 0<=nw<M and not visited[nh][nw] and not visitedWall[nh][nw]:
                #벽을 만났으면 현재 탐색하고자 하는 빈칸에 인접한 벽이므로 해당 벽의 위치를 추가함
                if arr[nh][nw] > 0:    
                    #print("wall")
                    walls.append([nh, nw])
                    visitedWall[nh][nw] = 1
                #빈칸을 만났으면 스택에 추가함 
                else:  
                   # print("blank")
                    visited[nh][nw] = 1 
                    stack.append([nh, nw])
                    sizeOfBlank += 1
       # print()
    blankSize.append(sizeOfBlank)
    adjWall.append(walls)

main()
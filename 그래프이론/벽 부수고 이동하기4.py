'''
빈칸에서 출발해 인접한 벽들을 표시하고, 빈 칸 수를 셈.
빈칸 수를 다세면 인접한 벽들에 빈칸 수를 더함.
'''

from re import L
import sys
import time
from collections import deque
t = time.time()
#input = sys.stdin.readline
sys.stdin = open("input.txt", "r")
#print = sys.stdout.write
N, M = 0,0
maxTime= 0
maxSize = 0
bnum = 0
visited =  []
arr =[]
adjWall, blankSize = [],[]
N, M = map(int, input().split())
MAP_SIZE = N*M
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = (list(map(int, input().strip())))
blankMap = [ [-1 for _ in range(M)] for _ in range(N)]
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
            bnum += 1
            T = time.time()
            stack = [[h,w]]
            visited[h][w] = 1
            sizeOfBlank = 1
            # visitedWall = [[0 for _ in range(M)] for _ in range(N)]
            #dfs 로 빈칸을 탐색하면서 벽을 만났을때, 빈칸을 만났을 때 다른 작업을 수행
            numLoop = 0
            while(stack):
                #print(stack)
                numLoop += 1
                h,w = stack.pop()
                #print("new:", h, w)
                for dh, dw in zip([0, 1, 0 ,-1], [1,0,-1, 0]):
                    nh,nw = h+dh, w+dw
                    #print(nh, nw)
                    if 0<=nh<N and 0<=nw<M:
                        #벽을 만났으면 현재 탐색하고자 하는 빈칸에 인접한 벽이므로 해당 벽의 위치를 추가함
                        # if arr[nh][nw] > 0 and not visitedWall[nh][nw]:
                        #     #print("wall")
                        #     walls.append([nh, nw])
                        #     visitedWall[nh][nw] = 1
                        #빈칸을 만났으면 스택에 추가함 
                        if arr[nh][nw] == 0 and not visited[nh][nw]:  
                        # print("blank")
                            visited[nh][nw] = 1 
                            stack.append([nh, nw])
                            sizeOfBlank += 1
            blankMap[h][w] = [sizeOfBlank, bnum]
            # print()
            cur += 1
print(blankMap)

for i in range(N):
    for j in range(M):
        if arr[i][j] > 0:
            done = []
            for dh, dw in zip([0, 1, 0 ,-1], [1,0,-1, 0]):
                nh,nw = i+dh, j+dw
                if 0<=nh<N and 0<=nw<M and blankMap[nh][nw] != -1 and  blankMap[nh][nw][1] not in done:
                    arr[i][j] += blankMap[nh][nw][0]
                    done.append(blankMap[nh][nw][1])


for i in range(N):
    print("".join(map(str,arr[i])))

'''
46003
00732
06040
50403
'''
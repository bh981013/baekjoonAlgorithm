import sys
#input = sys.stdin.readline
sys.setrecursionlimit(1000000)
sys.stdin = open("input.txt", "r")

'''
downMode 와 upMode로 나뉘어서, 한번 끝나면 계산함.
prev 와 cur을 비교해서 현재 모드와 대소관계를 비교함. ->틀린 풀이
'''
arr = []
H, W = 0,0
def calc(l, r):
    ret = 0
    h = min(arr[l], arr[r])
    for i in range(l ,r+1):
        remain = h - arr[i]
        if(remain > 0):
            ret += remain
    #print(ret)
    return ret

def main():
    global arr,H,W
    H, W = map(int, input().split())
    arr = list(map(int, input().split()))
    N = len(arr)
    prev = arr[0]
    indexL, indexR = 0,0    #왼쪽과 오른쪽의 범위
    isDown = -1 #상승/하강 여부 확인
    ret = 0
    for i in range(1, N):
        cur = arr[i]
        if(prev < cur): #올라감
            if isDown == 1: #내려가는 모드이면
                isDown = 0 #올라가는 모드로 바꿈
        elif(prev > cur):   #내려감
            if isDown == 0: #올라가는 모드이면, 한번의 웅덩이가 생겼기때문에 빗물의 양 계산
                indexR = prev
                ret+= calc(indexL, indexR)    #양 index 사이 빗물의 양 계산.
                indexL = i-1 #다시 indexL을 설정
                isDown = 1
            elif isDown == -1:  #초기조건. prev의 index가 indexL이 됨
                
                indexL = i-1
                isDown = 1
        #print(arr[i], isDown)
        prev = cur
    if(isDown == 0):
        #print("최종", indexL, N-1)
        ret+=calc(indexL, N-1)
    print(ret)

main()

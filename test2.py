arr = []
n = 0
ans = 0
def main():
    global arr, n, ans
    n = int(input())
    arr = list(map(int, input().split()))
    recur(-1, 0, 0)

    print(ans)

def recur(pickedIndex, S, pickCnt):
    global arr, n, ans
    if pickCnt == 3 and 2000<=S <= 2500:
        ans+=1
    for i in range(pickedIndex+1, n):
       recur(i, S+arr[i], pickCnt+1)
        
if __name__=="__main__":
    main()
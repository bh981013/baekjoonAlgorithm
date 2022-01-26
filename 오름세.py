'''
최장 증가 수열 문제의 답을 찾아야함.
하지만 일반적으로 알고있는 dp로 해결시,n^2의 시간복잡도를 갖으므로 10000개의 input이 넘어가면 사용할 수 없음
그래서 이진탐색을 통해 해당 값이 들어갈 만한 자리를 lower bound를 계산해서 집어넣음 -> lower bound, upper bound 구하는 법 꼭 기억하기!!
'''


import sys
#input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def lower_bound(arr, length, target):
    low, high = 0, length
    while(low<high):
        mid = (low+high)//2
        if arr[mid] >= target:
            high = mid
        else:
            low = mid + 1
    return low

def main():
    lines = sys.stdin.readlines()
    for i in range(len(lines)//2):
        arr = list(map(int,lines[2*i + 1].strip().split()))
        s = []
        for a in arr:
            idx = lower_bound(s, len(s),a)
            # print("idx:", idx)
            if idx == len(s):
                s.append(a)
            else:
                s[idx] = a
            # print(s)
            # print()
        
        print(len(s))

main()

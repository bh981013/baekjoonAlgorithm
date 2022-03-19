'''
사고과정:

브루트-포스로 모든 경우의 수를 구해볼까?->너무 경우의 수가 많음(약 N^2)
그럼 그리디로 접근해서 규칙을 찾아볼까?-> 먼저 합칠수록 그 값이 계속 더해지므로, 결과를 최소화하려면 가장 작은 묶음을 먼저 비교해야겠다!
그 결과를 계속 반영하면서 비교해야 하니까, 우선순위 큐를 활용!

우선순위 큐를 활용하여 구현

1. 가장 작은 두 묶음을 뽑는다
2. 두 묶음 크기를 더한 값을 정답에 더한다
3. 두 묶음을 더한값을 큐에 넣는다
4. 큐가 빌때까지 반복한다.
'''

import sys
import heapq
input = sys.stdin.readline

def main():
    N = int(input())
    arr = []
    for _ in range(N):
        heapq.heappush(arr, int(input()))
    answer = 0
    while(True):
        pop1 = heapq.heappop(arr)
        if arr:
            pop2 = heapq.heappop(arr)
            answer += pop1 + pop2
            heapq.heappush(arr, pop1+pop2)
        else:
            break
    print(answer)
    
main()

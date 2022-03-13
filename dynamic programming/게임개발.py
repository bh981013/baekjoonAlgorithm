'''
need 배열이 0 인 노드부터 하나씩 결과에 추가함
중요: 나보다 먼저 만들어져야 되는 것들 중 가장 오래걸리는 시간을 저장해야댐
'''
from re import T
import sys
from collections import deque
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")
def main():
    N = int(input())
    next = [[] for _ in range(N+1)]
    cost = [0]
    need = [0 for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    result = [0 for _ in range(N+1)]
    latest = [0 for _ in range(N+1)]
    q = deque()
    for i in range(1, N+1):
        temp = list(map(int, input().split()))
        cost.append(temp[0])
        curNeed = temp[1:-1]
        need[i] = len(curNeed)      #i번째 노드를 성립시키기 위해 필요핸 노드의 개수
        if need[i] == 0:
            q.append([i, cost[i]])
            visited[i] = True
        for n in curNeed:
            next[n].append(i)
    while(q):
        popped, c = q.popleft()
        result[popped] = c
        for n in next[popped]:
            need[n] -= 1
            latest[n] = max(latest[n], c)
            if not visited[n] and need[n] == 0:
                visited[n] = True
                q.append([n, latest[n] + cost[n]])
    print("\n".join(map(str, result[1:])))
main()
    
            


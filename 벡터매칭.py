'''
2개부터 N개까지 매칭 시킴
itertools를 이용한 풀이!
'''

import itertools
import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)

T = int(input())
result = []
for _ in range(T):
    N = int(input())
    answer = float("inf")
    points = [list(map(int, input().split())) for _ in range(N)]
    sumX = sum(list(map(lambda x: x[0], points)))
    sumY = sum(list(map(lambda x: x[1], points)))
    minSum = float("inf")
    for halfPoints in itertools.combinations(points, N//2):
        halfPointsSumX = sum(list(map(lambda x: x[0], halfPoints)))
        halfPointsSumY = sum(list(map(lambda x: x[1], halfPoints)))
        minSum = min(minSum, ((sumX-2 * halfPointsSumX) **
                     2 + (sumY-2*halfPointsSumY) ** 2) ** 0.5)
    print(minSum)

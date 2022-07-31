import heapq
import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**8)


class node:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def __lt__(self, other):
        if self.A > other.A:
            return True
        elif self.A == other.A:
            return self.B < other.B


def solution(genres, plays):
    answer = []
    N = len(genres)
    genresSizeMap = {}
    genresMaxMusicMap = {}
    for i, items in enumerate(zip(genres, plays)):
        g, p = items
        if genresSizeMap.get(g):
            genresSizeMap[g] += p
        else:
            genresSizeMap[g] = p
        if genresMaxMusicMap.get(g):
            h = genresMaxMusicMap[g]
            heapq.heappush(h, node(p, i))
        else:
            h = []
            heapq.heappush(h, node(p, i))
            genresMaxMusicMap[g] = h
    genresSizeArr = list(zip(genresSizeMap.keys(), genresSizeMap.values()))
    genresSizeArr.sort(key=lambda x: -x[1])
    for g, s in genresSizeArr:
        for i in range(2):
            if genresMaxMusicMap.get(g):
                answer.append(heapq.heappop(genresMaxMusicMap.get(g)).B)
    return answer


print(solution(["classic", "pop", "classic",
      "classic", "pop"], [500, 600, 150, 800, 2500]))

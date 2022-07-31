import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**8)


def solution(sticker):
    answer = 0
    N = len(sticker)
    if(N <= 3):
        return max(sticker)
    dp = [[0 for _ in range(N-3)] for _ in range(3)]
    for i in range(3):
        dp[i][0] = sticker[i+1]
        dp[i][1] = max(sticker[i+1:i+3])
    for i in range(3):
        for j in range(2, N-3):
            dp[i][j] = max(dp[i][j-2] + sticker[j+1+i], dp[i][j-1])
    for i in range(-1, 2):
        answer = max(sticker[i] + dp[i+1][-1], answer)
    #     print(i, answer)
    # print("\n".join(map(str, dp)))
    return answer


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))

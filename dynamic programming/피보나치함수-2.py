'''
n번째 0,1호출 횟수를 저장함.

'''
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def main():
    TC = int(input())
    output = []
    for _ in range(TC):
        n = int(input())
        dp = [[0, 0] for _ in range(n+1)]
        if(n == 0):
            output.append([1, 0])
            continue
        elif(n == 1):
            output.append([0, 1])
            continue
        dp[0] = [1, 0]
        dp[1] = [0, 1]
        for nth in range(2, n+1):
            dp[nth][0] = dp[nth-1][0] + dp[nth-2][0]
            dp[nth][1] = dp[nth-1][1] + dp[nth-2][1]
        output.append(dp[n])
    for out in output:
        print(" ".join(map(str, out)))


main()

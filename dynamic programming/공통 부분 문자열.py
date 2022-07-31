import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**5)

s1 = input().rstrip()
s2 = input().rstrip()
dp = [[0 for _ in range(len(s1))] for _ in range(len(s2))]
for i in range(len(s2)):
    for j in range(len(s1)):
        if(s2[i] == s1[j]):
            if(i-1 >= 0 and j-1 >= 0):
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = 1

# print("\n".join(map(str, dp)))
print(max(map(max, dp)))

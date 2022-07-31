import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt")
sys.setrecursionlimit(10**8)


def calcWholeTime(building):
    global numBuilding, needBuildings, dp, buildTimes
    maxTime = 0
    if(dp[building] != -1):
        return dp[building]
    for need in needBuildings[building]:
        maxTime = max(calcWholeTime(need), maxTime)
    dp[building] = maxTime + buildTimes[building]
    # print(f'calc:{building}, result: {maxTime}')
    return dp[building]


TC = int(input())
output = []
for _ in range(TC):
    numBuilding, numRules = map(int, input().split())
    buildTimes = [0] + list(map(int, input().split()))
    needBuildings = [[] for _ in range(numBuilding+1)]
    dp = [-1 for _ in range(numBuilding+1)]
    for _ in range(numRules):
        start, end = map(int, input().split())
        needBuildings[end].append(start)
    # print("needBuilings", needBuildings)
    target = int(input())
    output.append(calcWholeTime(target))
print("\n".join(map(str, output)))

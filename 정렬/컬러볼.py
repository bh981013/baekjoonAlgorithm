'''
전체 정렬 후 누적합과
각 색깔별 정렬 후 누적합을 계산해
전체-색 을통해 누적합을 구함
'''
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    arr = []
    for i in range(N):
        arr.append([i] + list(map(int, input().split()))) # [공번호, 색깔, 크기]
    perColor = [[] for _ in range(N+1)]
    for num, color, size in arr:
        perColor[color].append([num, size])
    
    # 크기 기준으로 전체 오름차순 정렬
    arr.sort(key = lambda x: x[2])

    # 전체 누적합 계산
    prefixSum = [arr[0][2]]
    for i in range(1, N):
        prefixSum.append(prefixSum[i-1] + arr[i][2])

    # 크기 기준으로 색깔별 오름차순 정렬
    for colorArr in perColor:
        colorArr.sort(key = lambda x: x[1])

    # 색깔별 누적합 계산
    prefixSumPerColor = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        if perColor[i]:
            prefixSumPerColor[i].append(perColor[i][0][1])
        for j in range(1, len(perColor[i])):
            prefixSumPerColor[i].append(prefixSumPerColor[i][j-1] + perColor[i][j][1])
    
    # 전체-색별
    answer = [0 for _ in range(N)]
    for i in range(N-1):
        num, color, size = arr[i]
        answer[num] += prefixSum[-1] - prefixSum[i+1]
        for j in range(len(perColor[color])-1):
            num, size = perColor[color][j]
            answer[num] -= prefixSumPerColor[color][-1] - prefixSumPerColor[color][j+1]

    print(answer)
    
main()
    
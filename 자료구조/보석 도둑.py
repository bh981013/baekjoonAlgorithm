import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
def main():
    goldNum, bagNum = map(int, input().split())
    golds = []
    bags = []
    for i in range(goldNum):
        weight, cost = map(int, input().split())
        golds.append([weight, cost])
    for i in range(bagNum):
        size = int(input())
        bags.append(size)
    bags.sort(reverse=True)
    golds.sort(key = lambda x:-x[0])
    candidate = []
    result = 0

    while(bags and len(candidate) + len(golds) != 0):
        bag = bags.pop()
        # print("bag: ", bag)
        if golds:
            gold = golds[-1]
            while(gold[0] <= bag):  #만약 보석의 무게가 가방보다 작다면
                gold = golds.pop()
                # print("candidate: ", gold)
                heapq.heappush(candidate, -gold[1]) #보석을 후보에 올려놓음
                if not golds: break
                gold = golds[-1]
        if candidate:
            popped = heapq.heappop(candidate)
            # print("popped: ", popped)
            result -= popped
    print(result)


main()
            


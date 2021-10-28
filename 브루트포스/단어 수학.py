import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
def main():
    dic = {}
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(reversed(input().strip())))
    arr.sort(key=len)
    for w in arr:
        for i in range(len(w)): #i+1번째 자리
            if(dic.get(w[i]) == None):
                dic[w[i]] = 10**(i)
            else: dic[w[i]] += 10**(i)
    l = list(zip(dic.keys(), dic.values()))
    l.sort(key=lambda x:-x[1])
    result = 0
    for i in range(len(l)):
        result += (l[i][1] * (9-i))
    print(result)
main()
            


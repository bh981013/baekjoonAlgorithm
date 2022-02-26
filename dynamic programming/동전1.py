import sys
input = sys.stdin.readline
cache = []
def get_cache(i):
    if i>= 0: return cache[i]
    else: return 0
def main():
    global cache
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    cache = [0 for _ in range(k+1)]
    cache[0] = 1    # 0을 만들수 있는 경우는 아무것도 안쓰는경우이므로 1가지
    for a in arr:
        for i in range(k+1):
            cache[i] = get_cache(i) + get_cache(i-a)
    print(cache[k])
main()
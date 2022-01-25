'''
stack을 사용하여, 뒤에서부터 스택에 넣음.
만약 자기보다 큰 수를 만났다면 해당 수가 정답
자기보다 작거나 같다면 pop을 함
'''
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def main():
    N = int(input())
    arr = list(map(int, input().split()))
    stack = []
    answer = []
    for a in reversed(arr):
        answer.append(NGE(stack, a))
    print(" ".join(map(str, reversed(answer))))

def NGE(stack, num):
    while(stack):
        top = stack[-1]
        if top > num:
            stack.append(num)
            return top
        else:
            stack.pop()
    stack.append(num)
    return -1            

main()            
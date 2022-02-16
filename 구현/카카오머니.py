import sys
input = sys.stdin.readline
def gcd(a,b):
    if(b == 0):
        return a
    else:
        return gcd(b, a%b)

def main():
    n = int(input())
    last_b = 0
    minb = 10 ** 18
    pay = None
    valid = True
    for _ in range(n):
        a,b = map(int,input().split())
        if a+last_b<0:  #충전이 필요함
            temp = b-a-last_b   #충전 금액
            if b != 0 and b<minb:
                 minb=b
            if pay == None:
                pay = temp
            else:
                pay = gcd(pay,temp) # 최대공약수 구하기
            if pay <= minb and minb != pow(10,18):
                valid = False
                break
        else: 
            if last_b + a != b:
                valid =False
                break
        last_b = b
    if not valid: print(-1)
    elif not pay: print(1)
    elif valid: print(pay)
    

main()
import sys
# input = sys.stdin.readlines
# sys.stdin = open("input.txt", "r")
D = {}
SQUARE = 1
LOWER_TRI = 2
UPPER_TRI = 3
SMALL_TRI = 4

FIRST_SHORTCUT = 5
SECOND_SHORTCUT = 10
FASTEST_SHORTCUT = 8

def cnt0(string):
    ret = 0
    for s in string:
        if s == '0':    #뒷면인 경우
            ret += 1
    if ret == 0:
        return 5
    else: return ret

def recur(string):
    if len(string) == 4:
        D[string] = cnt0(string)
    else:
        recur(string + '0')
        recur(string + '1')

def main():
    recur("")
    remain = 10
    lines = sys.stdin.readlines()#pop 사용하기 위해 뒤집음
    lines.reverse()
    mode = SQUARE
    cur = 0
    WIN = False
    while(remain > 0 and lines):
        move = D[lines.pop().strip()]
        if move >=4:
            remain += 1
        cur += move
        if mode == SQUARE:
            if cur == FIRST_SHORTCUT:
                mode = LOWER_TRI
            elif cur == SECOND_SHORTCUT:
                mode = UPPER_TRI
        elif mode == LOWER_TRI and cur == FASTEST_SHORTCUT:
            mode = SMALL_TRI

        if  mode == SQUARE and cur > 20 or \
            mode == UPPER_TRI and cur > 16 or \
            mode == LOWER_TRI and cur > 16 or \
            mode == SMALL_TRI and cur > 11:
            WIN = True
            break
    if WIN:
        print("WIN")
    else: print("LOSE")            

main()
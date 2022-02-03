import sys
# sys.stdin = open("input.txt", "r")

WIN = 0
DRAW = 1
LOSE = 2
games = []
prob = [[[WIN, DRAW, LOSE] for _ in range(6)] for _ in range(4)]
answer = [0 for _ in range(4)]

def main():
    global games, prob, answer
    name = input().strip().split()
    dic = {}
    for i, n in enumerate(name):
        dic[n] = i
    for _ in range(6):
        n1, n2, W, D, L = input().strip().split()
        i1 = dic[n1]
        i2 = dic[n2]
        games.append([i1, i2])
        prob[i1][i2][WIN] = float(W)
        prob[i1][i2][DRAW] = float(D)
        prob[i1][i2][LOSE] = float(L)

        prob[i2][i1][WIN] = float(L)
        prob[i2][i1][DRAW] = float(D)
        prob[i2][i1][LOSE] = float(W)
    recursive_loop([])
    print("\n".join(map(str,answer)))

def recursive_loop(result):
    global games,prob,answer
    if len(result) == 6:
        P = 1
        point = [0 for _ in range(4)]
        for g,r in zip(games, result):
            P *= prob[g[0]][g[1]][r]
            if r == WIN:
                point[g[0]] += 3
            elif r == DRAW:
                point[g[0]] += 1
                point[g[1]] += 1
            else:
                point[g[1]] += 3
        D = [0,0,0,0]
        for i in range(4):
            rank = 1
            dup = 1
            for j in range(4):
                if i == j:
                    continue
                if point[i] < point[j]:
                    rank+=1
                elif point[i] == point[j]:
                    dup+=1
            if rank == 1:
                if dup  <= 2:
                    answer[i] += (P)
                elif dup >2 : 
                    answer[i] += (P*2/dup)
            elif rank == 2:
                answer[i] += P/dup
            D[i] = [rank, dup]
        # if sum(result)== 0:
        #     print(result)
        #     print(point)
        #     print(answer)
        #     print(D)
        return
    else:
        for r in range(3):
            recursive_loop(result + [r])

main()
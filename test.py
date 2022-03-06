
levels = []
keys = []
state = []
sumState = []

def main():
    global levels, state, keys, sumState
    numLevel, numOp = map(int, input().split())
    levels = [0] + list(map(int, input().split()))
    levels.append(10**10)
    state = [{}]+ [{} for _ in range(numLevel+1)]
    keys = [[] for _ in range(numLevel+1)]
    sumState = [0 for _ in range(numLevel+1)]

    output = []
    for _ in range(numOp):
        op = input().split()
        if op[0] == "I":
            insert(int(op[1]), int(op[2]))
        else:
            f = find(int(op[1]), numLevel)
            if f == None:
                output.append("none")
            else: output.append(" ".join(map(str, f)))
    print("\n".join(output))


def insert(key, size):
    global levels, state, sumState, keys
    level = 1
    succ = insertLev(level, key, size)
    while(not succ):
        succ = True
        for k in keys[level]:
            succ = succ and insertLev(level+1, k, state[level][k])
        state[level] = {}
        keys[level] = []
        sumState[level] = 0
        level += 1


def insertLev(lev, key, size):
    global levels, state, sumState, keys
    got = state[lev].get(key)
    if got:
        state[lev][key] = size
        sumState[lev] = sumState[lev] - got + size
    else:
        state[lev][key] = size
        sumState[lev] += size
        keys[lev].append(key)
    if sumState[lev] > levels[lev]:
        return False
    else: return True

def find(key, numLevel):
    global state
    for l in range(1, numLevel+1):
        f =  state[l].get(key)
        if f:
            return [l, f]
    return None

if __name__=="__main__":
    main()
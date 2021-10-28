import sys
myinput = sys.stdin.readline
sys.setrecursionlimit(100000)
output = []
#sys.stdout.write()
children = []
def main():
    global children
    numNodes = int(input())
    children = [[] for _ in range(numNodes)]
    parent = list(map(int, input().split()))
    for i in range(numNodes):
        if parent[i] != -1:
            children[parent[i]].append(i)
    numLeaf = 0
    for ch in children:
        if not ch:
            numLeaf += 1
    # print(children)
    target = int(input())
    if parent[target] == -1:
        print(0)
    elif len(children[parent[target]]) == 1:
        print(numLeaf - getNumLeaf(target) + 1)
    else:
        print(numLeaf - getNumLeaf(target))

def getNumLeaf(node):
    global children
    num = 0
    if not children[node]:
        return 1
    else:
        for ch in children[node]:
            num += getNumLeaf(ch)
    return num
main()


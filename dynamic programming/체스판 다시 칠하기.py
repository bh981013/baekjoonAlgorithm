import copy
a = input().split()
b = []
for i in a:
    b.append(int(i))

b2 = []
for i in range(b[0]):
    t = input()
    b2.append(t)
n1 = b[0]
n2 = b[1]
c1, c2 = [],[]
for j in range(n1):
    d1, d2 = [], []
    for i in range(n2):
        if (j%2 == 0 and i % 2 == 1 and b2[j][i] == 'W') or (j%2 == 0 and i % 2 == 0 and b2[j][i] == 'B')or (j%2 == 1 and i % 2 == 1 and b2[j][i] == 'B') or (j%2 == 1 and i % 2 == 0 and b2[j][i] == 'W'):
            d1.append(1)
            d2.append(0)
        elif (i % 2 == 1 and b2[j][i] == 'B') or (i % 2 == 0 and b2[j][i] == 'W') or (j%2 == 1 and i % 2 == 1 and b2[j][i] == 'W') or (j%2 == 1 and i % 2 == 0 and b2[j][i] == 'B'):
            d2.append(1)
            d1.append(0)
    c1.append((d1))
    c2.append((d2))

sum = 64
for i in range(n1-7):
    for j in range(n2-7):
        temp1, temp2 =0,0
        for k in range(i, i+8):
            for k2 in range(j, j+8):
                temp1 +=c1[k][k2]
                temp2 += c2[k][k2]
        if(sum>(min(temp1, temp2))): sum = min(temp1, temp2)
print(sum)

import copy
a = int(input())
b = []
for i in range(a):
    k  = input()
    b.append(k)
#b2 = list(set(b))
b2 = {}
for i in b:
    b2[i] = len(i)
b2 = b2.items()
q = sorted(b2, key=lambda x: (x[1], x[0]))
for j in [i[0] for i in q]:
    print(j)

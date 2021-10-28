import copy
a = input().split()
b = []
for i in a:
    b.append(int(i))

print(min(b[0], b[2]-b[0], b[1], b[3]-b[1]))

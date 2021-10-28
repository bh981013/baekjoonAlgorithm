a = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            a.append(f"{i}{j}{k}666")
for i in range(10):
    for j in range(10):
        for k in range(10):
            a.append(f"{i}{j}666{k}")
for i in range(10):
    for j in range(10):
        for k in range(10):
            a.append(f"{i}666{j}{k}")
for i in range(10):
    for j in range(10):
        for k in range(10):
            a.append(f"666{i}{j}{k}")
b = list(set(a))
temp = []
for j in range(1,3):
    for i in b:
        temp.append(f"{j}{i}")
c = b+temp
c1 = []
for i in c:
    c1.append(int(i))
c1.sort()

i = int(input())
print(int(c1[i-1]))


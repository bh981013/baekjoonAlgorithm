a = input().split()
b = []
for i in a:
    b.append(int(i))
c = (b[1] ** 2) + (b[2] ** 2)
x = (b[0]**2) / c
x = x ** 0.5
print(int(b[1]*x), int(b[2]*x))

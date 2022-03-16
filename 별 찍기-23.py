n = int(input())
for i in range(n):
    if i==0:
        for _ in range(n):
            print("*", end ="")
        for _ in range(n):
            print(" ", end ="")
        for _ in range(n):
            print("*", end ="")
    else:
        print(" "*i, end="")
        print("*", end="")
        print(" "* (n-2), end = "")
        print("*", end="")
        
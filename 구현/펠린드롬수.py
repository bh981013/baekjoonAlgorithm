x = []
while(True):
    a  = (input())
    if a == "0": break
    else: x.append(a)
for i in x:
    t = "yes"
    for k in range(int(len(i)/2)):
        if i[k] != i[len(i) -k-1]:
            t = "no"
            break
    print(t)




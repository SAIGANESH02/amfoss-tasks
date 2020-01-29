n = int(input())
for k in range(0,n):
    a = int(input())
    b = []
    x = 0
    for i in range(1,a):
        if i%5== 0:
            b.append(i)
        elif i%3 == 0:
            b.append(i)
    l = len(b)
    for j in range(0,l):
        x = x + b[j]
    print(x)
    
n = int(input())
for k in range(0,n):
    
    a = int(input())
    b = []
    for i in range(1,a):
        if a % i == 0:
           b.append(i)
    b.sort()
    l = len(b)
    if l > 1:
        print(b[-1])
    else:
        print(a)
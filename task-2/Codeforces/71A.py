
i = int(input())
j = 1
for j in range(i):
    b = input()
    arr = list(b)
 
    l = int(len(arr))
    f = str(l-2)
    if l>10:
        print(arr[0]+ f +arr[l-1])
    else :
        print(b)
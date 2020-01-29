n = int(input())



s = 0

s1 = 0



for i in range(0, n):

    

    arr = input()

    arr1 = list(map(int,arr.split(" ")))

    
    v = i

    s = arr1[v] + s


    v1 = n - i - 1

    s1 = arr1[v1] + s1
    
if s > s1:
    print(s - s1)
else:
    print(s1 - s)

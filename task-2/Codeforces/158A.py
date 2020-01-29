a = input()
arr = list(map(int,a.split(" ")))
n = arr[0]
s = arr[1]
i = 0
sel = 0
p = input()
arr1 = list(map(int,p.split(" ")))

for i in range(n):
        if arr1[i] >= s:
            sel += 1
        else:
            sel = 0

print(sel)
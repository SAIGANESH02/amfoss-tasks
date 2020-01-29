y = int(input())
b = "X++"
c = "--X"
x = 0
i = 1
for i in range(y):
    
    a = input()
    
    if b in a:
        x+=1
    
    elif c in a:
        x-=1
print(x)
    
    
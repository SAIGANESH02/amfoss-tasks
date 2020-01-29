
i = input()
arr = list(map(int,i.split(" ")))
n = arr[0]
m = arr[1]
a = arr[2]

if(n%a == 0):    
    b = (n//a)
    
else:
    b = ((n//a)+1)

if(m%a == 0):   
    c = (m//a)

else:
    c = ((m//a)+1)

print(b*c)  
arr = input()

a = list(map(int,arr.split()))

arr = input()

b = list(map(int,arr.split()))

if a[0] > b[0]:

    ap = 1

    bp = 0

if a[0] < b[0]:

    ap = 0

    bp = 1

if a[0] == b[0]:

    ap = 0

    bp = 0

if a[1] > b[1]:

    ap = ap + 1

    bp = bp + 0

if a[1] < b[1]:

    ap = ap + 0

    bp = bp + 1

if a[1] == b[1]:

    ap = ap + 0

    bp = bp + 0

if a[2] > b[2]:

    ap = ap + 1

    bp = bp + 0

if a[2] < b[2]:

    ap = ap + 0

    bp = bp + 1

if a[2] == b[2]:

    ap = ap + 0

    bp = bp + 0

print(ap,bp)



n = int(input())

s = 1

for s in range(1, n+1):

    for j in range(1, n-s+1):

        print(" ", end='')

    k = 0

    while k != s:

        print("#", end='')

        k = k + 1

    print("")
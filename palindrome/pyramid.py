n = int(input())


spaces = 2*(n-1)
for i in range(1, n+1):
    print(" "*spaces, end="")
    if i == 1:
        print(1, end="")
    else:
        for j in range(1, i+1):
            print(str(j) + " ", end="")
        for j in range(i-1, 0, -1):
            print(str(j) + " ", end="")
    spaces -= 2
    print()
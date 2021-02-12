n = int(input())

spaces = 2*(n-1)
for i in range(1, n+1):
    print(" "*spaces, end="")
    if i == 1:
        print("1")
    else:
        for j in range(i, 2*i):
            print(str(j) + " ", end="")
        for j in range(2*i-2, i-1, -1 ):
            print(str(j) + " ", end="")
        print()
    spaces -= 2
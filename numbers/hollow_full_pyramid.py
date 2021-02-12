n = int(input())

spaces = n-1
for i in range(1, n+1):
    print(" "*spaces, end="")
    if i == n:
        for j in range(1,i+1):
            print(str(j) + " ", end="")
    else:
        for j in range(1, i+1):
            if j == 1 or j == i:
                print(str(j) + " ", end="")
            else:
                print("  ", end="")
    spaces -= 1
    print()

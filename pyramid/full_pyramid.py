n = int(input())

spaces = n
for i in range(n):
    print(" "*spaces, end="")
    for j in range(i+1):
        print("*",end=" ")
    spaces -= 1
    print()
    
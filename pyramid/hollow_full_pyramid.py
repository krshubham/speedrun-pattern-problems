n = int(input())

spaces = n
for i in range(1,n+1):
    print(" "*spaces, end="")
    if i == 1 or i == n:
        print("* "*i, end="")
    else:
        print("*" + " "*(2*i-3) + "*",end="")
    print()
    spaces -= 1
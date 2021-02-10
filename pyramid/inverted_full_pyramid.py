n = int(input())

spaces = 0
for i in range(n,0,-1):
    print(" "*spaces, end="")
    print("* "*i,end="")
    print()
    spaces += 1
n = int(input())

inner_spaces = 2*n-5
for i in range(1, n+1):
    if i == 1:
        for j in range(1, n+1):
            print(str(j) + " ", end="")
    elif i == n:
        print(n,end="")
    else:
        print(i, end="")
        print(" "*inner_spaces,end="")
        inner_spaces -= 2
        print(n,end="")
    print()
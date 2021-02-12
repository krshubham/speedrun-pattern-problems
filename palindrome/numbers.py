n = int(input())

for i in range(1, n+1):
    if i == 1:
        print(1, end="")
    else:
        for j in range(1, i+1):
            print(str(j) + " ", end="")
        for j in range(i-1, 0, -1):
            print(str(j) + " ", end="")
    print()
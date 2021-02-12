n = int(input())


initial_ascii = 64
for i in range(1, n+1):
    if i == 1:
        print(chr(initial_ascii + 1), end="")
    else:
        for j in range(1, i+1):
            print(chr(initial_ascii + j) + " ", end="")
        for j in range(i-1, 0, -1):
            print(chr(initial_ascii + j) + " ", end="")
    print()
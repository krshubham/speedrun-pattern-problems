rows = int(input())
columns = int(input())

for i in range(rows):
    if i == 0 or i == rows - 1:
        for j in range(columns):
            print("*", end=" ")
    else:
        for j in range(columns):
            if j == 0 or j == columns-1:
                print("*", end=" ")
            else:
                print(" ",end=" ")
    print("")
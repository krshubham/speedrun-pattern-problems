n = int(input())

for i in range(n, 1, -1):
    if(i == n):
        print("*"*i)
        continue
    print("*" + " "*(i-2) + "*")
print("*")
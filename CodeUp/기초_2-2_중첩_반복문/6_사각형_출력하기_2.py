a = int(input())

for i in range(a) :
    print("*" * a if i == 0 or i == a - 1 else "*" + " " * (a - 2) + "*")

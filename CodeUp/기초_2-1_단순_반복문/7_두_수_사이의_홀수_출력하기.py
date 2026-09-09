a, b = input().split()
a, b = int(a), int(b) + 1

while (a < b) :
    if (a % 2 == 1) :
        print(a, end =" ")
    a += 1
    
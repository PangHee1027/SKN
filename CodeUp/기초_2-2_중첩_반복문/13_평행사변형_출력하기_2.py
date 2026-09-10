a, b, c = input().split()
a, b = int(a), int(b)

if c == "L" :
    for i in range(a) :
        print(" " * i + "*" * b)
else :
    for i in range(a) :
        print(" " * (a - i - 1) + "*" * b)

a, b = input().split()
i = float(a)
j = float(b)

while (i <= j) :
    print(format(i, "0.2f"), end =" ")
    i += 0.01
    
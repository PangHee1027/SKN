a, b = input().split()
i = min([int(a), int(b)])
j = max([int(a), int(b)]) + 1

while (i < j) :
    print(i, end =" ")
    i += 1
    
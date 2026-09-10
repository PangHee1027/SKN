n, m = map(int, input().split())

for i in range (1, m + 1) :
    for j in range (1, n + 1) :
        if (i == 1 and j == 1) or (j == 1 and i == m) :
            print("+", end = "")
        elif (i == m and j == n) or (j == n and i == 1) :
            print("+")
        elif i == 1 or i == m :
            print("-", end = "")
        elif j == 1 :
            print("|", end = "")
        elif j == n :
            print("|")
        else :
            print(" ", end = "")

a = int(input())
result = [[" " for i in range(a)] for j in range(a)]

for i in range(a) :
    for j in range(a) :
        if i == 0 or i == a - 1 :
            result[i][j] = "*"
        elif i == a // 2 :
            result[i][j] = "*"
        else :
            if j == 0 or j == a - 1 :
                result[i][j] = "*"
            elif j == i :
                result[i][j] = "*"
            elif a - j - 1 == i :
                result[i][j] = "*"
            elif j == a // 2 :
                result[i][j] = "*"

for i in result :
    for j in i :
        print(j, end = "")
    print()